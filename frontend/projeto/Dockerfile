FROM node:18-alpine

#RUN mkdir front
WORKDIR /usr/src/app

COPY ./package.json .
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]



