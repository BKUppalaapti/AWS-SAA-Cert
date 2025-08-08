import boto3
import json

# Initialize CloudFormation client
cf = boto3.client('cloudformation')

# Define the CloudFormation template
template_body = json.dumps({
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Create S3 bucket, EC2 instance, and Security Group",
    "Resources": {
        "MyS3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "BucketName": "bala-clfn-s3-bucket"
            }
        },
        "MySecurityGroup": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "Allow SSH access",
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 22,
                        "ToPort": 22,
                        "CidrIp": "0.0.0.0/0"
                    }
                ]
            }
        },
        "MyEC2Instance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "ImageId": "ami-0c94855ba95c71c99",  # Replace with a valid AMI ID for your region
                "InstanceType": "t2.micro",
                "SecurityGroups": [{"Ref": "MySecurityGroup"}]
            }
        }
    }
})

# Create the stack
response = cf.create_stack(
    StackName='MyMultiResourceStack',
    TemplateBody=template_body,
    Capabilities=['CAPABILITY_NAMED_IAM'],  # Required if using IAM resources
)

print("Stack creation initiated. Stack ID:", response['StackId'])