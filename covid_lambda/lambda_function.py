import json
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    data = response.json()

    s3 = boto3.client('s3')
    bucket_name = "covid-etl-data-ankit"  # replace with your S3 bucket name
    file_name = f"raw/covid_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(data)
    )

    return {"status": "success", "file": file_name}
