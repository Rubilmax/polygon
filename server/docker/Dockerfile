FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /polygon-server

# Build context: ./server
COPY ./Makefile .
COPY ./requirements.txt .

RUN apt-get update
# Python & MySQL dev headers for Debian / Ubuntu
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y

RUN make install
