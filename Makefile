STACKNAME_BASE="gimmeatroll"
REGION="us-east-2"
URL="gimmeatroll.com"
ZONE="gimmeatroll.com."
BUCKET="gimmeatroll"

all: deploy-apigw

prep:
	cd lambda && \
		zip -r9 /tmp/zipfile.zip * && \
		aws s3 cp --region $(REGION) /tmp/zipfile.zip \
			s3://$(BUCKET)/$(shell md5sum lambda/* | md5sum | cut -d ' ' -f 1) && \
		rm -f /tmp/zipfile.zip

deploy-apigw: deploy-acm prep
	aws cloudformation deploy \
		--template-file apigw-lambdas.yml \
		--stack-name $(STACKNAME_BASE)-com \
		--region $(REGION) \
		--parameter-overrides "DomainName=$(URL)" \
		"ZoneName=$(ZONE)" \
		"Bucket=$(BUCKET)" \
		"md5=$(shell md5sum lambda/* | md5sum | cut -d ' ' -f 1)" \
		--capabilities CAPABILITY_IAM || exit 0

deploy-acm:
	# Only works in us-east-1
	aws cloudformation deploy \
		--template-file acm_certs.yml \
		--stack-name $(STACKNAME_BASE)-acm-certs \
		--region us-east-1 \
		--parameter-overrides "ACMUrl=$(URL)" \
		--capabilities CAPABILITY_IAM || exit 0
