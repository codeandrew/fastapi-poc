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




<!-- LINKS -->
[fastapi-0]: ./uploads/fastapi-flow.jpeg
[fastapi-1-docs]: ./uploads/fastapi-docs.png
