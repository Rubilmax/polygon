start-server:
	docker-compose up -d --build polygon-server

start-client:
	docker-compose up -d --build polygon-client

start-db:
	docker-compose up -d --build polygon-db

start:
	docker-compose up -d --build
