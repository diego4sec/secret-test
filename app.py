import boto3
from botocore.config import Config

AWS_ACCESS_KEY = "secret1"
AWS_SECRET_KEY = "secret2"
AWS_REGION     = "us-east-2"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

# Example: list all S3 buckets
def list_s3_buckets():
    s3 = session.client("s3", config=Config(retries={"max_attempts": 10}))
    resp = s3.list_buckets()
    return [b["Name"] for b in resp.get("Buckets", [])]

if __name__ == "__main__":
    print("Buckets:", list_s3_buckets())
