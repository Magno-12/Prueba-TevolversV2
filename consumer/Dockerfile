FROM python:3.9
RUN mkdir /usr/src/consumer/
COPY . /usr/src/consumer/
WORKDIR /usr/src/consumer/
EXPOSE 5200:5200
RUN pip install -r requirements.txt
CMD [ "uvicorn" "app:app", "--host", "0.0.0.0", "--port", "5200" ]
