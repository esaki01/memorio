# memorio/infra

## Environments
- Public Cloud: Google Cloud Platform
- Provisioning: Terraform

## Project usage
### Setup project
```
$ cd src
$ terraform init
```

### Select gcp project
```
$ terraform workspace list
$ terraform workspace select ${ENV}
```

### Confirm changes
```
$ terraform plan
```

### Change resources
```
$ terraform apply
```