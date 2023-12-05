FROM node:21-alpine3.17

RUN mkdir -p /root/.config/.wrangler/config
WORKDIR /usr/src/app
EXPOSE 8787
EXPOSE 8976
COPY package*.json ./
RUN npm install wrangler --save-dev
RUN npm install

COPY . .

CMD [ "npm", "run","dev" ]
#CMD [ "npm","run","deploy"]

