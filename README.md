# DevOps_Exercise

**Author:** Francisco Suarez
**Requirements:**
- anyio==3.6.1
- attrs==22.1.0
- certifi==2022.6.15
- charset-normalizer==2.1.1
- click==8.1.3
- fastapi==0.79.1
- h11==0.13.0
- httptools==0.4.0
- idna==3.3
- iniconfig==1.1.1
- packaging==21.3
- pluggy==1.0.0
- prometheus-client==0.14.1
- py==1.11.0
- pydantic==1.9.2
- pyparsing==3.0.9
- pytest==7.1.2
- python-dotenv==0.20.0
- PyYAML==6.0
- requests==2.28.1
- sniffio==1.2.0
- starlette==0.19.1
- tomli==2.0.1
- typing-extensions==4.3.0
- urllib3==1.26.11
- uvicorn==0.18.2
- uvloop==0.16.0
- watchfiles==0.16.1
- websockets==10.3

**Deploy:** `uvicorn main:app --reload`

**Test:** 
- On local host `http://localhost:8000/docs`
- On Heroku `https://devopsfs.herokuapp.com/docs`
- Metrics on `http://localhost:8001/`