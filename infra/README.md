# memorio/infra
Cloud infrastructure of memorio.

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

## Others
```
# encrypt secrets by kms api
$ gcloud kms encrypt --location global --keyring secrets-key-ring --key firebase-key --plaintext-file secrets.js --ciphertext-file secrets.js.encrypted
```