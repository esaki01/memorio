# parrot/backend
Backend application of parrot.

## Environments
- Programming language: Python 3.7
- Framework: Flask 1.1

## Project setup
```
# install requirements
$ pip install pipenv
$ pipenv install

# activate
$ pipenv shell
```

### Container
```
# build docker image
$ docker build -t $(DOCKER_TAG_NAME) .
```

## Run application
```
# compiles and hot-reloads
$ python app.py
```

### Container
```
# run docker container
$ docker container run -p 5000:5000 $(DOCKER_TAG_NAME)
```

## Others
```
# lint
$ pycodestyle src/
```