resource "google_cloudbuild_trigger" "frontend-deploy" {
  description = "frontend deploy"

  trigger_template {
    branch_name = "${lookup(var.build_trigger_branch, "${terraform.workspace}")}"
    repo_name   = "github_esaki01_parrot-front"
  }

  included_files = [
    "*",
  ]

  substitutions = {
    _GCP_PROJECT_ID = "${data.google_project.project.project_id}"
  }

  filename = "cloudbuild.yaml"
}

resource "google_cloudbuild_trigger" "backend-deploy" {
  description = "backend deploy"

  trigger_template {
    branch_name = "${lookup(var.build_trigger_branch, "${terraform.workspace}")}"
    repo_name   = "github_esaki01_parrot-api"
  }

  included_files = [
    "*",
  ]

  substitutions = {
    _GCP_PROJECT_ID = "${data.google_project.project.project_id}"
  }

  filename = "cloudbuild.yaml"
}
