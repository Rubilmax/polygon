start-server:
	cd server && make start

start-client:
	cd client && yarn start

start:
	docker-compose up -d --build
