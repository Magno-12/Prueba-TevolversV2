FROM python:3.9
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]