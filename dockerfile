FROM node:latest
ENV PORT=8000
COPY . /var/www
WORKDIR /var/www/
RUN npm install --unsafe-perm
EXPOSE $PORT
ENTRYPOINT ["npm", "start"]
