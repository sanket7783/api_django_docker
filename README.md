# api_django_docker
Its a basic implementation of django rest api with docker. It support different rest api operations like get,post,put,delete.

Steps to run this 
1. create a docker image
``` sudo  docker build -t docker_image_name -f Dockerfile .```
2. do docker run using following command
```sudo  docker run -it -p 8888:8888 docker_image_name```
note: 8888 are port here you need to provide this to access the application from your docker to host browser
Also if not installed please go through the docker installation guide here [docker installation](https://docs.docker.com/engine/install/)
3. supported api
    - http:0.0.0.0:8888/events/
    - http:0.0.0.0:8888/events/1/
