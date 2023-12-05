FROM node:21-alpine3.17

WORKDIR /usr/src/app
EXPOSE 8000
COPY package*.json ./
RUN npm install

COPY . .

CMD [ "npm", "run","dev" ]
CMD [ "npm","run","deploy"]

