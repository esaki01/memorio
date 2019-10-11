# infra

## Project setup
```
$ cd src
$ terraform init
```

## Select gcp project
```
$ terraform workspace list
$ terraform workspace select ${ENV}
```

## Confirm changes
```
$ terraform plan
```

## Change resources
```
$ terraform apply
```