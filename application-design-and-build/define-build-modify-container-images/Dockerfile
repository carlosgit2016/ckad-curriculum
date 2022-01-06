# Multi Stage container
FROM node:17 as base
WORKDIR /app
COPY k8s-container-image-example/ ./
RUN ["npm", "install", "-g", "gatsby-cli"]
RUN ["npm", "install"]

FROM node:17 as build
WORKDIR /app
COPY --from=base /app ./
RUN ["npm", "run-script", "build"]

FROM python:3.8.10-alpine as final
WORKDIR /app/www
COPY --from=build /app/public/ ./
ENTRYPOINT ["python", "-m", "http.server", "80"]