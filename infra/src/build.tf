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
  }

  filename = "frontend/cloudbuild.yaml"
}