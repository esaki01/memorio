resource "google_kms_key_ring" "secrets_key_ring" {
  project  = "${data.google_project.project.project_id}"
  name     = "secrets-key-ring"
  location = "us-central1"
}

resource "google_kms_crypto_key" "secrets_key" {
  name     = "secrets-key"
  key_ring = "${google_kms_key_ring.secrets_key_ring.id}"
}
