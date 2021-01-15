FROM python:3.9

WORKDIR /polygon-server

# Build context: ./server
COPY ./Makefile .
COPY ./requirements.txt .

RUN make install
