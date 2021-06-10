# Project Purple Cow

Creates an AWS API Gateway to check the SSL status of a given URL.

#### Details

![](/img/solution-6c245.png)

[https://07trrx9k3k.execute-api.us-east-1.amazonaws.com/prod/ssl-check?url=https://www.google.com](https://07trrx9k3k.execute-api.us-east-1.amazonaws.com/prod/ssl-check?url=https://www.google.com)

##### Assumptions

- API path will be `/ssl-check?url=https://www.google.com`
- No authentication required to use the API

##### Future Updates
  - Add CloudFormation Stack
  - Create proper authentication methods

##### Notes

The main feature missing from this POC is the ability to deploy it using CloudFormation. Due to time constraints I was unable to reliably get the CloudFormation stack working. This API is accessible by anyone and in the future versions of it, it should have proper authentication checks implemented.
