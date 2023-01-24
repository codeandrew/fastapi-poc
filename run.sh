#!/bin/bash 

#uvicorn main:app --reload
# PRODUCTION
#CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

docker run -p 80:80 -v $(pwd):/app fastapi:1
