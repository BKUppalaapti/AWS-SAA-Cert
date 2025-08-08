import boto3
import time

# Initialize CloudFormation client
cf = boto3.client('cloudformation', region_name='us-east-1')  # Change region if needed

# Stack parameters
stack_name = 'bala-s3-stack'
template_file = 's3-cfn.yaml'

# Read the template body
with open(template_file, 'r') as file:
    template_body = file.read()

# Create or update the stack
try:
    print(f"Creating stack: {stack_name}")
    response = cf.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Capabilities=['CAPABILITY_NAMED_IAM'],
    )
except cf.exceptions.AlreadyExistsException:
    print(f"Stack {stack_name} already exists. Updating...")
    response = cf.update_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Capabilities=['CAPABILITY_NAMED_IAM'],
    )

# Wait for completion
print("Waiting for stack operation to complete...")
waiter = cf.get_waiter('stack_create_complete')
waiter.wait(StackName=stack_name)
print(f"Stack {stack_name} deployed successfully.")