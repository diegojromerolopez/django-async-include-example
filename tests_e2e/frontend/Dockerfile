FROM node:18
WORKDIR /app
COPY tests_e2e/frontend/package.json ./
COPY tests_e2e/frontend/package-lock.json ./
COPY tests_e2e/frontend/jest.config.js ./
RUN npm install
COPY tests_e2e/frontend/entrypoint.js ./
