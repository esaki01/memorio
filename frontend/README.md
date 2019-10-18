# memorio/frontend
Frontend application of memorio.

## Environments
- Programming language: JavaScript, HTML, CSS
- Framework: Vue, Bulma
- Platform: Node.js
- Web server: nginx

## Project setup
```
# install requirements
$ npm install
```

### Container
```
# build docker image
$ docker build -t $(DOCKER_TAG_NAME) .
```

## Run application
```
# compiles and hot-reloads
$ npm run serve
```

### Container
```
# run docker container
$ docker container run -p 8080:8080 $(DOCKER_TAG_NAME)
```

## Others
```
# compiles and minifies
$ npm run build

# lint
$ npm run lint
```