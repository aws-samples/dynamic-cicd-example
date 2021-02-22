import boto3
import os
from awspolicy import BucketPolicy, KmsPolicy
aws_partition = os.environ['awspartition']

def lambda_handler(event, context):
    acc_id=''
    s3_client = boto3.client('s3')
    bucket_name = os.environ['artifactBucket']
    
    # Load the bucket policy as an object
    bucket_policy = BucketPolicy(serviceModule=s3_client, resourceIdentifer=bucket_name)
    
    # Select the statement that will be modified
    statement_to_modify = bucket_policy.select_statement('grant artifact bucket permissions')
    
    # Insert new_role_arn into the list of Principal['AWS']
    new_role1_arn = 'arn:%s:iam::%s:role/cicd-codepipeline-cfn-role' %(aws_partition, acc_id)
    new_role2_arn = 'arn:%s:iam::%s:role/cicd-lambda-copyartifact-role' %(aws_partition, acc_id)
    statement_to_modify.Principal['AWS'].append(new_role1_arn)
    statement_to_modify.Principal['AWS'].append(new_role2_arn)
    
    # Save change of the statement
    statement_to_modify.save()
    
    
    # Save change of the policy. This will update the bucket policy
    statement_to_modify.source_policy.save()
    print('saved bucket policy')
    
    ### Update KMS Key policy to allow a new account to use somaglobal-codebuild-cmk CMK
    kms = boto3.client('kms')
    cmk_policy = KmsPolicy(serviceModule=kms, resourceIdentifer= os.environ['CMKArn'])
    statement = cmk_policy.select_statement('Allow use of the key')
    new_acct = 'arn:%s:iam::%s:root' %(aws_partition, acc_id) 
    statement.Principal['AWS'].append(new_acct)
    statement.save()
    statement.source_policy.save()
    
    statement = cmk_policy.select_statement('Allow attachment of persistent resources')
    new_acct = 'arn:%s:iam::%s:root' %(aws_partition, acc_id)  
    statement.Principal['AWS'].append(new_acct)
    statement.save()
    statement.source_policy.save()
    print('saved kms policy')
