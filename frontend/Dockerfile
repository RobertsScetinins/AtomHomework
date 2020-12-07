FROM node:14.15.1-buster-slim

RUN mkdir /build-dir
WORKDIR /build-dir
COPY package.json /build-dir
RUN npm i npm@latest -g && \
    npm install -g @angular/cli@11.0.3
RUN npm install

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN ln -s /build-dir/node_modules node_modules

# Bundle app source
COPY . /usr/src/app

EXPOSE 1234
CMD [ "npm", "start" ]