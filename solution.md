# Project Purple Cow

Creates an AWS API Gateway to check the SSL status of a given URL.

#### Details

![](/img/solution-6c1e4.png)

```
aws cloudformation create-stack --stack-name PPC --template-body file://projectpurplecow_cf.yaml  --capabilities

aws cloudformation create-stack --stack-name PPC --template-body file://projectpurplecow_cf.yaml  --capabilities

URL="$(aws cloudformation describe-stacks --stack-name PPC --query 'Stacks[0].Outputs[0].OutputValue' | cut -d '"' -f 2)/v01/ssl-check"

curl -s $(echo "${URL}?url=google.com")

{"hostname": "google.com", "validFrom": "2021-05-17 01:36:58", "validTo": "2021-08-09 01:36:57", "expired": false}
```

##### Assumptions

- API path will be `v01/ssl-check?url=https://www.google.com`
- No authentication required to use the API

##### Future Updates
  - Create proper authentication methods

##### Notes

This stack does not contain proper authentication and access controls and thus should not be used in production.
