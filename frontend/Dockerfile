# Work with the latest node image.
FROM node:latest
# Add src code and create a dir called "app" in the image.
WORKDIR /app
# Copies the dependencies json to the root of the image.
COPY package.json ./
# Installs dependencies.
RUN npm install
# Copies all local files in the local dir to the /app dir. 
COPY . .
# Runs 'npm start'
CMD ["npm", "start"]