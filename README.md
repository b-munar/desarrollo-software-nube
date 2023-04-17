
Para levantar los servicios es necesario tener docker-compose descargado y ejecutar los siguientes comandos:

> docker compose build

> docker compose up -d
 
 o

> docker-compose build

> docker-compose up -d

Despues de desplegar, se debe importar el documento de postman y seguir la documentación, recomendamos hacer primero Sign UP, luego Log In, y despues Create New Task para consumir los otros Ent Points. Recomendamos que suba un archivo de su computador en el Create New Task, este no debe de sobrepasar los 20 mb, el nginx lo rechazaria. 

Para utilizar flower, ir al bash del server,

> docker exec -it "id desarrollo-software-nube-api-1" bash

y escribir en ese bash,

> celery -A tasks.compress.celery flower  --address=0.0.0.0 --port=5566

Para utilizar prometheus, en una terminal a nivel de sistema

> docker run --name Prometheus -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml -p 9090:9090 --network host prom/prometheus
