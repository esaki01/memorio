# PARROT/Infra
Cloud infrastructure of PARROT.

## Environments
- Public Cloud: Google Cloud Platform
- Provisioning: Terraform

## Project setup
```
# init terraform
$ cd src
$ terraform init

# select workspace
$ terraform workspace list
$ terraform workspace select ${ENV}
```

## Confirm state
```
$ terraform plan
```

## Apply state
```
$ terraform apply
```

## Encrypt secrets
```
# encrypt secrets file by kms api
$ gcloud kms encrypt --location us-central1 --keyring secrets-key-ring --key secrets-key --plaintext-file secrets.js --ciphertext-file secrets.js.encrypted

# encript secrets string by kms api
$ echo -n <secret-string> | gcloud kms encrypt --location us-central1 --keyring secrets-key-ring --key secrets-key --plaintext-file - --ciphertext-file - | base64
```