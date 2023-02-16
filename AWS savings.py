import boto3

# create clients for each AWS account
client1 = boto3.client('s3', aws_access_key_id='ACCESS_KEY_ID_1', aws_secret_access_key='SECRET_ACCESS_KEY_1')
client2 = boto3.client('s3', aws_access_key_id='ACCESS_KEY_ID_2', aws_secret_access_key='SECRET_ACCESS_KEY_2')
client3 = boto3.client('s3', aws_access_key_id='ACCESS_KEY_ID_3', aws_secret_access_key='SECRET_ACCESS_KEY_3')

# initialize total storage to 0
total_storage = 0

# get the sizes of all objects in each bucket in each account
for client in [client1]:
    response = client.list_buckets()
    for bucket in response['Buckets']:
        objects = client.list_objects(Bucket=bucket['Name'])['Contents']
        for obj in objects:
            total_storage += obj['Size']

# convert total storage from bytes to gigabytes
total_storage_gb = total_storage / (1024 ** 3)

# print the total storage in gigabytes
print(f"Total storage across three AWS accounts: {total_storage_gb:.2f} GB")
