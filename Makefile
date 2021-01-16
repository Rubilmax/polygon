start-server:
	cd server && make start

start-client:
	cd client && yarn start

start-db:
	docker-compose up -d --build polygon-db

start:
	docker-compose up -d --build
