# fastapi-poc

## Setup 
python3 -m venv .venv


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
