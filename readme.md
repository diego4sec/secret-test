demo repo to check and demo secrets scanning capability of legit 
instructions 
1. make sure that legit pr checks for secrets is enabled
2. create a new branch
3. copy the below text to a new python and commit
###########################################







##################################################



###############################################
#sample credentials 
[default]
aws_access_key_id = AKIA2T2SJH6M6OG5YL6T
aws_secret_access_key = BYMUjAx63HSt2Ctg6Q4Tq8AfitenrH1oAqbscqKq
output = json
region = us-east-2

import boto3
from botocore.config import Config
AWS_ACCESS_KEY = AKIA2T2SJH6M6OG5YL6T
AWS_SECRET_KEY = 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
AWS_REGION     = "us-east-2"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def list_s3_buckets():
    s3 = session.client("s3", config=Config(retries={"max_attempts": 10}))
    resp = s3.list_buckets()
    return [b["Name"] for b in resp.get("Buckets", [])]

if __name__ == "__main__":
    print("Buckets:", list_s3_buckets())
