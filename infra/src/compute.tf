resource "google_compute_instance" "default" {
  name         = "mysql"
  machine_type = "f1-micro"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = <<EOT
#!/bin/sh

sudo apt-get update

# install mysql
sudo apt-get -y install mysql-server 

# secure mysql
sudo apt-get -y install expect

export CURRENT_PASSWORD=""
export NEW_PASSWORD="${data.google_kms_secret.mysql_password.plaintext}"

expect -c "

set timeout 10

spawn sudo mysql_secure_installation

expect \"Enter current password for root (enter for none):\"
send \"$CURRENT_PASSWORD\r\"

expect \"Change the root password?\"
send \"y\r\"

expect \"New password:\"
send \"$NEW_PASSWORD\r\"

expect \"Re-enter new password:\"
send \"$NEW_PASSWORD\r\"

expect \"Remove anonymous users?\"
send \"y\r\"

expect \"Disallow root login remotely?\"
send \"y\r\"

expect \"Remove test database and access to it?\"
send \"y\r\"

expect \"Reload privilege tables now?\"
send \"y\r\"

expect eof
"

expect -c "

set timeout 10

spawn 

expect \"Enter password:\"
send \"$NEW_PASSWORD\r\"

expect eof
"

EOT
}

# decrypt mysql password
data "google_kms_secret" "mysql_password" {
  crypto_key = "${google_kms_crypto_key.secrets_key.id}"
  ciphertext = "${lookup(var.mysql, "password")}"
}

resource "google_compute_firewall" "default" {
  name    = "mysql-firewall"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["5000"]
  }
}
