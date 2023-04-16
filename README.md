Launch VS Code Quick Open (Ctrl+P), paste the following command, and press enter.
ext install ms-azuretools.vscode-docker

docker compose build
docker compose up -d

docker-compose build
docker-compose up -d 

docker logs --follow desarrollo-software-nube-api-1

celery -A tasks.compress.celery flower  --address=127.0.0.1 --port=5566
celery -A tasks.compress.celery flower  --address=0.0.0.0 --port=5566

docker exec -it 225a239006921167875fb56285fcda428355fb521af92c9e8554f87b27437d72 bash 

docker run --name Prometheus -v /home/brahi/repositories/desarrollo-software-nube/prometheus.yml:/etc/prometheus/prometheus.yml -p 9090:9090 --network host prom/prometheus

docker run --name Grafana -d -v grafana-storage:/var/lib/grafana  --network host grafana/grafana