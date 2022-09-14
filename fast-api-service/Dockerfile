FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . .
COPY ./.env /.env

EXPOSE 80:80