# project variables
GCP_PROJECT_ID=memorio-256321

# cloud run variables
CLOUD_RUN_REGION=us-central1
BACKEND_TAG_NAME=memorio/backend
FRONTEND_TAG_NAME=memorio/frontend

.PHONY: deploy-backend # Deploy backend
deploy-backend:
	gcloud builds submit --project $(GCP_PROJECT_ID) --tag gcr.io/$(GCP_PROJECT_ID)/$(BACKEND_TAG_NAME) ./backend && \
	gcloud beta run deploy backend --project $(GCP_PROJECT_ID) --image gcr.io/$(GCP_PROJECT_ID)/$(BACKEND_TAG_NAME) \
	--platform managed --region $(CLOUD_RUN_REGION) --allow-unauthenticated

.PHONY: deploy-frontend # Deploy frontend
deploy-frontend:
	gcloud builds submit --project $(GCP_PROJECT_ID) --tag gcr.io/$(GCP_PROJECT_ID)/$(FRONTEND_TAG_NAME) ./frontend && \
	gcloud beta run deploy frontend --project $(GCP_PROJECT_ID) --image gcr.io/$(GCP_PROJECT_ID)/$(FRONTEND_TAG_NAME) \
	--platform managed --region $(CLOUD_RUN_REGION) --allow-unauthenticated
