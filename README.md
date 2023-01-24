# fastapi-poc

## Overview

![fastapi-0]


## API Endpoints / Features

- USERS
  - create
  - get all
  - get {user_id}
- ITEMS
  - get
  - create
- FILES
  - upload Files

### API DOCUMENTATION

URL: `{$HOST}/docs`
![fastapi-1-docs]



## Setup 
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt 

# to run the application 
uvicorn main:app --reload
```

FOR DOCKERFILE

```
docker build -t fastapi:1 .  
docker run -p 80:80 fastapi:1 
```

## troubleshooting

to access requestion json use async and await 

```python
@app.post("/")
async def read_root(request: Request):
    header = request.headers
    client = request.client.host
    body =  await request.json()
```


## References

Accessing Request Headers:
https://stackoverflow.com/questions/68231936/how-can-i-get-headers-or-a-specific-header-from-my-backend-api

access whole body request

### Database Schema vs Pydantic Models

https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-7-sqlalchemy-database-setup/

### Authentication and SSO 

- https://blog.hanchon.live/guides/google-login-with-fastapi-and-jwt/
> Very Detailed 
 
- https://nilsdebruin.medium.com/fastapi-google-as-an-external-authentication-provider-3a527672cf33

- https://blog.authlib.org/2020/fastapi-google-login
> Very Bsic


### Security 
Securing salt has password 
https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python

### Deployment 

https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-13-docker-deploy/

## TO FOLLOW 
- https://www.youtube.com/watch?v=0_seNFCtglk&list=PLrOQsSoS-V69xir8m0LfdLDHG0ZAgCj2U

<!-- LINKS -->
[fastapi-0]: ./uploads/fastapi-flow.jpeg
[fastapi-1-docs]: ./uploads/fastapi-docs.png
