FROM python:3.12.0b1-slim 

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt; pwd; ls -latr

EXPOSE 80
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
