terraform {
  backend "gcs" {
    project = "parrot-256517"
    bucket  = "parrot-terraform-backend"
    prefix  = ""
  }
}
