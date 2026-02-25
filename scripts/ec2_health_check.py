import boto3

def check_ec2_instances():
    session = boto3.Session(profile_name="default")  # adjust if needed
    ec2 = session.client("ec2")

    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print("=" * 40)
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"State: {instance['State']['Name']}")
            print(f"Instance Type: {instance['InstanceType']}")
            print(f"Public IP: {instance.get('PublicIpAddress', 'None')}")
            print(f"Private IP: {instance.get('PrivateIpAddress', 'None')}")
            print(f"Security Groups: {[sg['GroupName'] for sg in instance['SecurityGroups']]}")
            print("=" * 40)

if __name__ == "__main__":
    check_ec2_instances()
