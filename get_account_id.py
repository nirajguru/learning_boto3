'''calling sts to get caller identity '''
import profile
import boto3

sts = boto3.client('sts')
#print(sts.get_caller_identity())
aws_acount_id = sts.get_caller_identity().get('Account')
print(f"Your AWS Account ID is {aws_acount_id}")
