import boto3
import os
region = 'ap-northeast-1'
instances = [os.environ['INSTANCE_ID']]

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    action = event["Action"]
    response = ec2.describe_instances(InstanceIds=instances)
    ec2_status = response['Reservations'][0]['Instances'][0]['State']['Name']
    print(instances[0] + ' instance is ' + ec2_status + ' now.')
    
    if action == "Start":
        ec2.start_instances(InstanceIds=instances)
        print('started your instance: ' + str(instances[0]))
    elif action == "Stop":
        ec2.stop_instances(InstanceIds=instances)
        print('stopped your instance: ' + str(instances[0]))
    else:
        print('Lamdba function could not be executed.')
