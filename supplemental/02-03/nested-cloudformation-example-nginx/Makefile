APPLICATION := bluejays
ROOT_DIR	:= $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PARENTDIR   := $(realpath ../)
AWS_REGION	:= us-west-2
GITHASH 	:= $(shell git rev-parse --short HEAD)
ENVIRONMENT := testing

# Location to publish templates for consumption
S3_PROD_BUCKET_NAME	:= cloudformation.us-west-2.258748242541.andrewkrug.com
S3_PROD_BUCKET_URI	:= s3://$(S3_PROD_BUCKET_NAME)/$(APPLICATION)

.PHONY:all
all:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]\.PHONY.*].*:' Makefile

.PHONY: publish
publish:
	@export AWS_REGION=$(AWS_REGION)
	aws s3 sync . $(S3_PROD_BUCKET_URI)/$(GITHASH) --exclude="*" --include="*.yml"
	aws s3 sync . $(S3_PROD_BUCKET_URI)/latest --exclude="*" --include="*.yml"

.PHONY: create-stack
create-stack:
	aws cloudformation create-stack \
	--stack-name mr-bluejays-latest-${ENVIRONMENT} \
	--template-url https://s3-us-west-2.amazonaws.com/${S3_PROD_BUCKET_NAME}/$(APPLICATION)/latest/mr-bluejays-parent.yml \
	--disable-rollback \
	--capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM

.PHONY: update-stack
update-stack:
	aws cloudformation update-stack \
	--stack-name mr-bluejays-latest-${ENVIRONMENT} \
	--template-url https://s3-us-west-2.amazonaws.com/${S3_PROD_BUCKET_NAME}/$(APPLICATION)/latest/mr-bluejays-parent.yml \
	--capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM

.PHONY: update-stack-with-changeset
update-stack-with-changeset:
	aws cloudformation create-change-set \
	--stack-name mr-bluejays-latest-${ENVIRONMENT} \
	--include-nested-stacks \
	--change-set-name mr-bluejays-latest-${ENVIRONMENT} \
	--template-url https://s3-us-west-2.amazonaws.com/${S3_PROD_BUCKET_NAME}/$(APPLICATION)/latest/mr-bluejays-parent.yml \
	--capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM

.PHONY: clean
clean:
	aws cloudformation delete-stack \
	--stack-name mr-bluejays-latest-${ENVIRONMENT}

.PHONY: lint
lint:
	cfn_nag *.yml
