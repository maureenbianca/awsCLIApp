# AWS CLI Application

## Overview
This App is a command line interface (CLI) application that would allow users to easily take inventory of all the resources that are currently provisioned in AWS environment. This guide walks you through installing and configuring the tool. After that, you can begin making calls to your AWS services from the command line.

##### Tested and deployed on Ubuntu OS
### Resources
          - IAM
          - EC2
          - RDS
          - S3
          - ECS
          - ECR

### Prerequisites

- Have an AWS account
- Install AWS cli
- Python
- Boto3

### Install prerequisites on the server

The aws-cli package works on Python versions:

- 2.7.x 
- 3.4.x
- 3.5.x
- 3.6.x 
- 3.7.x 
- 3.8.x 

Now, let's install aws-cli
```
$ sudo pip install awscli
```
Check version
```
$ aws --version
```
Install python on the server to enable you to get started using Boto3
```
$ apt install python
```
Boto3 is the AWS Software Development Kit (SDK) for Python, which allows to write software that makes use of service. Install the library
```
$ pip install -U boto3
```
### Getting started
Before using aws-cli, you need to tell it about your AWS credentials. You can do this by running the command below. Credentials are stored in ~/.aws/credentials by default

```
$ aws configure
```
### Usage

Unpack/Extract ICTlife application package
```
 $ git clone https://github.com/maureenbianca/awsApp.git
 $ cd awsApp
 $ python awsApp.py
  ``` 
 You can get help on the command line to see the supported services,
```
aws help
```
