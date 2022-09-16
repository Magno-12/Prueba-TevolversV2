FROM python:3.9
RUN mkdir /usr/src/consumer/
COPY . /usr/src/consumer/
WORKDIR /usr/src/consumer/
EXPOSE 5000
RUN pip install -r requirements.txt
CMD [ "python", "app.py"]