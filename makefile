build:
	docker build . -t mais-todos-api

run:
	sudo docker run -d --name api -p 8000:8000 mais-todos-api:latest

stop:
	sudo docker stop api && sudo docker rm api

test:
	docker exec api python -m pytest -v /src --disable-warnings
