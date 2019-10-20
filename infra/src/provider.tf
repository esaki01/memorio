provider "google" {
  credentials = "${file("${var.credential["${terraform.workspace}"]}")}"
  project     = "parrot-${lookup(var.project_number, "${terraform.workspace}")}"
  region      = "asia-northeast1"
}

provider "google-beta" {
  credentials = "${file("${var.credential["${terraform.workspace}"]}")}"
  project     = "parrot-${lookup(var.project_number, "${terraform.workspace}")}"
  region      = "asia-northeast1"
}
