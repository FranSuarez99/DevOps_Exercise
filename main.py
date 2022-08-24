import requests
import logging
from logging.config import dictConfig
from typing import Union
from prometheus_client import Counter, start_http_server
from fastapi import FastAPI
from pydantic import BaseModel # adicionar en los imports en el main.py
#from uicheckapp.services import EchoService

counterP = Counter('my_failures', 'Description of counter')
start_http_server(8001)

LOG_LEVEL: str = "DEBUG"
FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging_config = {
    "version": 1, # mandatory field
    # if you want to overwrite existing loggers' configs
    # "disable_existing_loggers": False,
    "formatters": {
        "basic": {
            "format": FORMAT,
        }
    },
    "handlers": {
        "console": {
            "formatter": "basic",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
            "level": LOG_LEVEL,
        }
    },
    "loggers": {
        "simple_example": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            # "propagate": False
        }
    },
}

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

app = FastAPI()
log = logging.getLogger("simple_example")

app.get("/")
def read_root():
    url = 'https://630287099eb72a839d7105f1.mockapi.io/items'
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json() }

@app.get("/log_now")
def log_now():
    log.debug("/api/log_now starts")
    log.info("I'm logging")
    log.warning("some warnings")
    counterP.inc()     # Increment by 1
    print(counterP)
    return {"result": "OK", "Counter": str(counterP)}

@app.get("/items")
def read_root():
    return [{"id": 1}, {"id": 2}]

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    url = 'https://630287099eb72a839d7105f1.mockapi.io/items'
    read_item = requests.get(url = url + '/' + str(item_id))
    #return {"item_id": item_id, "q": q}
    return{"items": read_item.json()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    url = 'https://630287099eb72a839d7105f1.mockapi.io/items'
    update_item = requests.put(url = url, data = item.json())
    return {"item_name": item.name, "item_id": item_id}

@app.delete("/items/{item_id}")
def delete_item(item_id: int, item: Item):
    url = 'https://630287099eb72a839d7105f1.mockapi.io/items'
    delete_item = requests.delete(url, json = item.json(), timeout =5)
    return Item.text

@app.post("/items/")
def save_item(item: Item):
    url = 'https://630287099eb72a839d7105f1.mockapi.io/items'
    new_item = requests.post(url, data=item.json(), timeout =5,  headers={'Content-Type': 'application/json'})
    print(item.json())
    return new_item.text
