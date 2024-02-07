upv:
	sudo docker-compose up -d --build

downv:
	sudo docker-compose down --remove-orphans

psv:
	sudo docker-compose ps

up:
	docker compose down --remove-orphans
	docker compose up -d --build
	docker compose ps

down:
	docker compose down --remove-orphans

ps:
	docker compose ps

main:
	sudo python main.py

loader:
	sudo cd db && sudo python loader.py

venv:
	sudo python3.11 -m venv venv

net:
	sudo docker network create nginx_proxy

9200:
	sudo lsof -i -P -n | grep 9200

8004:
	sudo lsof -i -P -n | grep 8004

log:
	sudo docker logs fastapi_5
