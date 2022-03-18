Building an Ecommerce API in GraphQL

- docker-compose build
- docker-compose up
- Change bucket policy on AWS to allow public access, so that you can save your static file on there and allow admin to render with the default django template
- docker-compose run --rm web python manage.py migrate  (web:service name to migrate to docker db)
- docker-compose run --rm web python manage.py createsuperuser_if_none_exists

#NOTE:
1. IF DOCKER IS RAISING PERMISSION DENIED LOCALLY, RUN:
- sudo chmod 666 /var/run/docker.sock

2. IF YOU WANT TO DROP A CONTAINER DB
-  To drop container db, delete container id for postgres and web and run ```docker-compose up``` again