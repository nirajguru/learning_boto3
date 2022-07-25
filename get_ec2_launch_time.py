'''Module for getting the launch time of an EC2 instance'''
import boto3

aws_mgmt_console = boto3.session.Session(profile_name='default')
ec2 = aws_mgmt_console.client('ec2')

for each_reservation in ec2.describe_instances().get('Reservations'):
    for each_instance in each_reservation.get('Instances'):
        instance_id = each_instance.get('InstanceId')
        instance_launch_time = each_instance.get('LaunchTime').strftime('%Y-%m-%d')
        instance_az = each_instance.get('Placement').get('AvailabilityZone')
        print("======================================")
        print(f"Instance {instance_id} launched on {instance_launch_time} in AZ {instance_az}")
