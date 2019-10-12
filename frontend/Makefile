# project variables
GCP_PROJECT_ID=memorio-253807

# cloud run variables
DOCKER_TAG_NAME=memorio/frontend

.PHONY: setup # Setup project
setup:
	npm install

.PHONY: run # Compiles and hot-reloads
run:
	npm run serve

.PHONY: build # Compiles and minifies
build:
	npm run build

.PHONY: lint # Lints and fixes files
lint:
	npm run lint

.PHONY: container-build # Build docker image
container-build:
	docker build -t $(DOCKER_TAG_NAME) .

.PHONY: container-run # Run docker container
container-run:
	docker container run -p 8080:8080 $(DOCKER_TAG_NAME)

.PHONY: deploy # Deploy application
deploy:
	gcloud builds submit --project $(GCP_PROJECT_ID) --tag gcr.io/$(GCP_PROJECT_ID)/$(DOCKER_TAG_NAME); \
	gcloud beta run deploy --project $(GCP_PROJECT_ID) --image gcr.io/$(GCP_PROJECT_ID)/$(DOCKER_TAG_NAME)