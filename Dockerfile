FROM python:3.9-slim 

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt; pwd; ls -latr

# CMD [ "uvicorn main:app --reload" ]
EXPOSE 80
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]