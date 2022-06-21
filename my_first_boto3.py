import boto3
import json

aws_mgmt_console = boto3.session.Session(profile_name='default')
aws_iam_console = aws_mgmt_console.client('iam')

#print(aws_mgmt_console.get_available_resources())
# This prints the available resources in the console
# Resource is a high level service available for ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']. All of operations
# are not available for resource

# Client is a low level service available for all AWS services. It returns a json object. As this is low level service, there is work needed to be done to parse the json object.
# All operations on the client are available for all AWS services.

my_user_list = aws_iam_console.list_users()['Users']

for every_user in my_user_list:
    print (every_user['UserName'])