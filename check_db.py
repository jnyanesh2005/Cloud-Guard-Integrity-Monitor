import boto3
from app.core.config import settings

def check_table_schema():
    print(f"Checking table: {settings.DYNAMODB_TABLE_NAME}")
    db = boto3.client(
        'dynamodb',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )
    try:
        response = db.describe_table(TableName=settings.DYNAMODB_TABLE_NAME)
        key_schema = response['Table']['KeySchema']
        print(f"Key Schema: {key_schema}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_table_schema()
