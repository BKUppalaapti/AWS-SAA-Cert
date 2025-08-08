import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def list_s3_buckets(profile_name=None):
    try:
        # Optional: Use a specific AWS profile
        if profile_name:
            session = boto3.Session(profile_name=profile_name)
            s3 = session.client('s3')
            print('session:',session)
        else:
            s3 = boto3.client('s3')
            print('else',s3)

        print("🔍 Fetching S3 buckets...")
        response = s3.list_buckets()

        buckets = response.get('Buckets', [])
        if not buckets:
            print("🚫 No buckets found in this AWS account.")
            return

        print("✅ S3 Buckets:")
        for bucket in buckets:
            name = bucket['Name']
            created = bucket['CreationDate'].strftime("%Y-%m-%d %H:%M:%S")
            print(f"- {name} (created on {created})")

    except NoCredentialsError:
        print("❌ AWS credentials not found. Run 'aws configure' or set environment variables.")
    except PartialCredentialsError:
        print("⚠️ Incomplete AWS credentials. Check your config.")
    except ClientError as e:
        print(f"❗ AWS Client error: {e}")
    except Exception as e:
        print(f"💥 Unexpected error: {e}")

if __name__ == "__main__":
    # Optional: pass a profile name like 'default' or 'dev'
    list_s3_buckets(profile_name=None)