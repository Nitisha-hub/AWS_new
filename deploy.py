import boto3

s3 = boto3.client('s3')

bucket_name = 'your-bucket-name'
file_name = 'index.html'

s3.upload_file(file_name, bucket_name, file_name)

print("Deployment successful 🚀")
