# Dynamic CI/CD Example

## Pre-requisites ##
* Ensure you have a BitBucket Cloud Account and Repository


## Instructions ##
1. Clone this repository
1. Unzip the dynamic-cicd-repo.zip file and push it to your Bitbucket repository
1. Follow this blog post to set up the dynamic multi-account pipeline

This is a sample repository to demonstrate a dynamic CI/CD deployment - Below is a brief explanation of the repository structure:
```bash
├── README.md                             # Readme file
├── cicd-grantpermission-function.zip     # This archive contains the code for deploying the cicd-grant-permission Lambda function in the main CI/CD account
├── cicd-mainaccount.yaml                 # This template is deployed in the main CI/CD account to create the CI/CD pipeline resources
├── cicd-targetaccount.yaml               # This template is deployed in the target CI/CD accounts to create the CI/CD pipeline resources
├── dynamic-cicd-repo.zip                 # This archive contains the source code for the sample application
│   ├── appfrontend          # Project directory for the front-end React App.
│   ├── buildspec.yml        # File containing the build commands and related settings that CodeBuild uses to run a build.
│   ├── hello-world          # Project directory for the back-end Go App.
│   └── template.yaml        # File to create the AWS CloudFormation package in the build stage.
