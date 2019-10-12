# project variables
GCP_PROJECT_ID=memorio-253807

# cloud run variables
DOCKER_TAG_NAME=memorio/backend

.PHONY: setup # Setup project
setup:
	pip install pipenv && \
	pipenv install && \
	pipenv shell

.PHONY: run # Compiles
run:
	python app.py

.PHONY: lint # Lints and fixes files
lint:
	pycodestyle src/

.PHONY: container-build # Build docker image
container-build:
	docker build -t $(DOCKER_TAG_NAME) .

.PHONY: container-run # Run docker container
container-run:
	docker container run -p 5000:5000 $(DOCKER_TAG_NAME)

.PHONY: deploy # Deploy application
deploy:
	gcloud builds submit --project $(GCP_PROJECT_ID) --tag gcr.io/$(GCP_PROJECT_ID)/$(DOCKER_TAG_NAME) && \
	gcloud beta run deploy --project $(GCP_PROJECT_ID) --image gcr.io/$(GCP_PROJECT_ID)/$(DOCKER_TAG_NAME)