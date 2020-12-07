FROM node:alpine
RUN apk update && apk add --no-cache make git

WORKDIR /frontend

COPY package.json package-lock.json /frontend/

RUN npm install -g @angular/cli@11.0.3

RUN chown -R node /frontend

WORKDIR /frontend

USER node

RUN npm install     