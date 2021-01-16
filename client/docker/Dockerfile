FROM node:12

WORKDIR /polygon-client

# Build context: ./client
COPY ./package.json .
COPY ./yarn.lock .

RUN yarn
RUN yarn global add @vue/cli-service
