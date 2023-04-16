Launch VS Code Quick Open (Ctrl+P), paste the following command, and press enter.
ext install ms-azuretools.vscode-docker

docker compose build
docker compose up -d

docker-compose build
docker-compose up -d 

docker logs --follow desarrollo-software-nube-api-1


celery -A utils.tasks_compress.celery worker -B -s /home/celery/var/run/celerybeat-schedule --loglevel INFO

docker exec -it 225a239006921167875fb56285fcda428355fb521af92c9e8554f87b27437d72 bash 