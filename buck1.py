import boto3


def create_bucket_and_upload_file():
    # region
    region = 'us-east-1'
    client = boto3.client('s3', region_name=region, endpoint_url=f"https://s3.{region}.amazonaws.com")

    #bucket name
    bucket_name = input("Enter the name of the bucket: ")

    # Create the bucket
    client.create_bucket(Bucket=bucket_name)
    print("Bucket created successfully.")

    file_path = 'C:\\Users\\AMRITA\\Documents\\AWS\\project boto3\\awswebsite project\\cab.jpg'
    object_name = "cab"

    # Upload the file to the bucket
    client.upload_file(file_path, bucket_name, object_name,ExtraArgs={'ContentType': 'text/html'})
    print("File uploaded successfully.")

    '''public access block for s3'''
    response = client.put_public_access_block(
    Bucket=bucket_name,
    # ContentMD5='string',
    # ChecksumAlgorithm='CRC32'|'CRC32C'|'SHA1'|'SHA256',
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls':False,
        'BlockPublicPolicy':False,
        'RestrictPublicBuckets':False
    },
    ExpectedBucketOwner='471112734926' #acc id aws
)
    print("public access block configured")
  

    '''deleting the file inside bucket'''

    # client.delete_object(Bucket=bucket_name, Key=object_name)
    # print("file deleted successfully")
    # '''delete bucket'''
    # client.delete_bucket(Bucket=bucket_name)
    # print('bucket deleted bucket')

    return bucket_name, object_name

if __name__ == "__main__":
    bucket_name, object_name = create_bucket_and_upload_file()
    print("Bucket Name:", bucket_name)
    print("Object Name:", object_name)









