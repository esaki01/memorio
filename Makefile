# project variables
GCP_PROJECT_ID=parrot-256516

# cloud run variables
CLOUD_RUN_REGION=us-central1
BACKEND_TAG_NAME=parrot/backend
FRONTEND_TAG_NAME=parrot/frontend

.PHONY: deploy-backend # Deploy backend
deploy-backend:
	gcloud builds submit --project $(GCP_PROJECT_ID) --tag gcr.io/$(GCP_PROJECT_ID)/$(BACKEND_TAG_NAME) ./backend && \
	gcloud beta run deploy parrot-api --project $(GCP_PROJECT_ID) --image gcr.io/$(GCP_PROJECT_ID)/$(BACKEND_TAG_NAME) \
	--platform managed --region $(CLOUD_RUN_REGION) --allow-unauthenticated

.PHONY: deploy-frontend # Deploy frontend
deploy-frontend:
	gcloud builds submit --project $(GCP_PROJECT_ID) --tag gcr.io/$(GCP_PROJECT_ID)/$(FRONTEND_TAG_NAME) ./frontend && \
	gcloud beta run deploy parrot --project $(GCP_PROJECT_ID) --image gcr.io/$(GCP_PROJECT_ID)/$(FRONTEND_TAG_NAME) \
	--platform managed --region $(CLOUD_RUN_REGION) --allow-unauthenticated
