FROM node:8.15.0-alpine

WORKDIR /app

COPY ./package.json .

RUN npm install

COPY . . 

CMD ["node", "main.js"]
