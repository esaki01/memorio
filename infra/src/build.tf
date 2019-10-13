resource "google_cloudbuild_trigger" "frontend-deploy" {
  description = "frontend deploy"

  trigger_template {
    branch_name = "${lookup(var.build_trigger_branch, "${terraform.workspace}")}"
    repo_name   = "github_esaki01_memorio"
  }

  included_files = [
    "frontend/**"
  ]

  substitutions = {
    _GCP_PROJECT_ID = "${data.google_project.project.project_id}"
  }

  filename = "frontend/cloudbuild.yaml"
}