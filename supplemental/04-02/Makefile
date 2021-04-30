APPLICATION := bluejays
ROOT_DIR	:= $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
AWS_REGION	:= us-west-2
ORG_ID 		:= aws organizations list-roots | jq '.Roots[0].Id' -r


.PHONY:all
all:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]\.PHONY.*].*:' Makefile

.PHONY:apply
apply:
	@echo 'Applying terraform to $(ORG_ID)'
	terraform apply -var-file tf.vars

.PHONY:plan
plan:
	@echo 'Applying terraform to $(ORG_ID)'
	terraform plan -var-file tf.vars