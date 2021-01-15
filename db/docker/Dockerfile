FROM mysql:5.7

# Build context: ./db
COPY ./populate.sql /docker-entrypoint-initdb.d/dump.sql
