FROM node:alpine
RUN mkdir /fs
RUN npm install node-sass npm-run-all --save-dev
ADD package.json /
CMD ["npm","start"]