# Dynamic CI/CD Example

## Pre-requisites ##
* Multiple AWS Accounts with Control Tower Setup
* BitBucket Account and Repository

## Instructions ##
* Clone the Repo
* Unzip the files 
* Commit the files to your BitBucket Repository
* Follow the blog post here:


This is a sample repository to demonstrate a dynamic CI/CD deployment - Below is a brief explanation of the repo structure:
```bash
.
├── appfrontend                 <-- Project directory for the front-end React App.
├── buildspec.yml               <-- File containing the build commands and related settings that CodeBuild uses to run a build.
├── hello-world                 <-- Project directory for the back-end Go App.
├── README.md                   <-- Readme file
└── template.yaml               <-- File to create the AWS CloudFormation package in the build stage of CodeBuild.
