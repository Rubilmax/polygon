FROM python:3.9

WORKDIR /polygon-server

RUN apt-get update
# Python & MySQL dev headers for Debian / Ubuntu
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y

# Build context: ./server
COPY ./Makefile .
COPY ./requirements.txt .

RUN make install

EXPOSE 5000
