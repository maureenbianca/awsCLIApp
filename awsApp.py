#!/usr/bin/env python3
# ICTlife CLI App
# @version 1.0
# @author Maureen <maureenchebett@gmail.com>
#the code displays a list of services i.e:
#IAM users, EC2 instances, S3 buckets, RDS instances, ECS clusters and ECR repositories
import boto3
#List s3 buckets
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
 print(bucket.name)

#List EC2 Instances
ec2 = boto3.resource('ec2')
for i in ec2.instances.all():
    print(i)

#List IAM users
client = boto3.client('iam')
try:
    user = client.list_users()
    for user in user['Users']:
        print(user['UserName'])
except Exception as error:
    print error

#List ECS Clusters
client = boto3.client('ecs')
clusters = client.list_clusters()
clusters_arns = clusters['clusterArns']
clusters_descriptions = client.describe_clusters(
    clusters=clusters_arns
)
#get ecs clusters
for cluster in clusters_descriptions['clusters']:
    print(cluster['clusterName'])

#List ECR Repositories
client = boto3.client('ecr')
try:
#get all ecr repositories
    repo = client.describe_repositories()
    for repo in repo['repositories']:
        print (repo['repositoryName'])
        
except Exception as error:
    print error

#List RDS Instances            
client = boto3.client('rds')
try:
# get a list of rds instances
    db = client.describe_db_instances()
    for db in db['DBInstances']:
        print (db['DBInstanceIdentifier'])
except Exception as error:
    print error

 #EOF
