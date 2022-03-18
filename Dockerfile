FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

# Install postgres client
RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

RUN mkdir /demo_graphql

WORKDIR /demo_graphql

COPY . /demo_graphql/

RUN adduser -D user

USER user