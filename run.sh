#!/bin/bash 

#uvicorn main:app --reload
docker build -t fastapi:1 .
docker run -p 80:80 -v $(pwd):/app\
    --env environment=test\
    --env app_version="23.01.25-43" fastapi:1  
