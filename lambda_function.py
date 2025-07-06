import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
table_name = os.environ.get('DDB_TABLE')
sns_topic = os.environ.get('SNS_TOPIC_ARN')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    name = body.get('name')
    email = body.get('email')
    message = body.get('message')

    table = dynamodb.Table(table_name)
    table.put_item(Item={
        'id': datetime.utcnow().isoformat(),
        'name': name,
        'email': email,
        'message': message
    })

    sns.publish(
        TopicArn=sns_topic,
        Message=f"New Feedback from {name} ({email}): {message}",
        Subject="New Feedback"
    )

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({"result": "Success"})
    }