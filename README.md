Para levantar los servicios es necesario tener docker-compose descargado y ejecutar los siguientes comandos:

> docker build -t server-image  .
> docker run --name server-container -it -e PORT=8080 -p 8080:8080 server-image