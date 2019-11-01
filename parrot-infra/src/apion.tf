data "google_project" "project" {}

resource "google_project_services" "project" {
  project  = "${data.google_project.project.project_id}"
  services = "${var.service}"

  provisioner "local-exec" {
    command = "sleep 30"
  }
}
