FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /demo_graphql

WORKDIR /demo_graphql

COPY . /demo_graphql/


RUN pip install --upgrade pip

#RUN adduser -D user
#
#USER user

RUN pip install -r requirements.txt

