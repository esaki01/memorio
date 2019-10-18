terraform {
  backend "gcs" {
    project = "memorio-255615"
    bucket  = "memorio-terraform-backend"
    prefix  = ""
  }
}
