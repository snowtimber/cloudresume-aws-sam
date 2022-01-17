# cloudresume-aws-sam
This is the backend to my cloud resume (https://heyitslogan.com/) using AWS SAM to create a visitor counter using
js <-> Api Gateway <-> lambda function (python) <-> DynamoDB

You can read my blog post at https://heyitslogan.com/journal.html.

Hey all, here is my attempt at Forrest Brazeal's #CloudResumeChallenge:

This repo is specific to my attempt to create the backend using dynamoDB, Lambda, AWS API gateways necessary for my cloud resume's visitor counter using AWS SAM.  Please see this link for the frontend code and my full experience building out this challenge -> https://github.com/MooseEagleShark/LoganTMeyerResume/

Here are the challenge requirements from Forrest's blogpost at: https://forrestbrazeal.com/2020/04/23/the-cloud-resume-challenge/

# GitHub Actions SAM Deployment Example
The purpose of this repository is to illustrate a GitHub Actions pipeline deploying a SAM template.

In this particular example we are deploying Amazon API Gateway, AWS StateMachine, AWS Lambda Functions, and corresponding IAM Roles.

## How it Works

There is one workflows `sam-validate-build-test-deploy`.

In this repository's current configuration, deployment occurs when changes land into the `main` branch. This is seen within the `.github/workflows/sam-validate-build-test-deploy.yml` file:
```
on:
  push:
    branches: [ main ]
```


## How To Configure
* Fork this repo and update the code and SAM template to reflect the code you are looking to deploy.
* Within the Repository settings for your fork or repo, create the following `Secrets` to configure the permissions to be used by the GitHub Actions pipeline:
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN
AWS_REGION
```

Please note the `AWS_SESSION_TOKEN` is optional, but preferable.
