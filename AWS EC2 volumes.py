import boto3

# create clients for each AWS account
client1 = boto3.client('ec2', aws_access_key_id='ACCESS_KEY_ID_1', aws_secret_access_key='SECRET_ACCESS_KEY_1', region_name='REGION_NAME_1')
client2 = boto3.client('ec2', aws_access_key_id='ACCESS_KEY_ID_2', aws_secret_access_key='SECRET_ACCESS_KEY_2', region_name='REGION_NAME_2')
client3 = boto3.client('ec2', aws_access_key_id='ACCESS_KEY_ID_3', aws_secret_access_key='SECRET_ACCESS_KEY_3', region_name='REGION_NAME_3')

# initialize total volume to 0
total_volume = 0

# get the volumes for all instances in each account
for client in [client1, client2, client3]:
    response = client.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            for volume in instance['BlockDeviceMappings']:
                total_volume += volume['Ebs']['VolumeSize']

# convert total volume from GB to TB
total_volume_tb = total_volume / 1024

# print the total volume in TB
print(f"Total volume across three AWS accounts: {total_volume_tb:.2f} TB")
3