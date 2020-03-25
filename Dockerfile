FROM python:3.7

RUN apt install -y git

RUN pip install gitpython

WORKDIR /code