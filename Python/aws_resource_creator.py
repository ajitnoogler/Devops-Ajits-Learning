import boto3

def create_s3_bucket(bucket_name, region='ap-south-1'):
    s3 = boto3.client('s3', region_name=region)
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
        print(f"S3 bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print("Error creating S3 bucket:", e)

def create_ec2_instance(image_id='ami-0c55b159cbfafe1f0', instance_type='t2.micro'):
    ec2 = boto3.resource('ec2')
    try:
        instance = ec2.create_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1
        )
        print(f"EC2 instance created with ID: {instance[0].id}")
    except Exception as e:
        print("Error creating EC2 instance:", e)

def main():
    print("What do you want to create?")
    print("1. S3 Bucket")
    print("2. EC2 Instance")

    choice = input("Enter choice (1/2): ")

    if choice == '1':
        bucket_name = input("Enter S3 bucket name: ")
        create_s3_bucket(bucket_name)
    elif choice == '2':
        create_ec2_instance()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()


