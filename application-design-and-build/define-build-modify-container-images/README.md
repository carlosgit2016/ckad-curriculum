### Multi Stage image
Each stage is a build stage and we can re use the things generated between the differents stages, that helps keeping the image optmized and easy to read and maintain

### Docker context
A context is where the docker will look from the filesystem to initiate a build and sends it for the Docker daemon, usually the context is your current working directory and you can specific where is your Dockerfile passing `-f` when using `docker build`