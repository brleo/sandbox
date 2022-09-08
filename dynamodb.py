import boto3
import decimal
import secrets

from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from datetime import datetime

def replace_decimals(obj):
    if isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = replace_decimals(obj[i])
        return obj
    elif isinstance(obj, dict):
        for k in obj.iterkeys():
            obj[k] = replace_decimals(obj[k])
        return obj
    elif isinstance(obj, decimal.Decimal):
        if obj % 1 == 0:
            return int(obj)
        else:
            return float(obj)
    else:
        return obj

def get_random_names(table_name, total_items = 1):
    
    if total_items > 100:
        return("The limit of parameter 'total_items' is 100.")

    dynamodb_object = boto3.resource('dynamodb')
    dynamodb_client = boto3.client('dynamodb')
    
    table = dynamodb_object.Table(table_name)
    
    try:
        response = dynamodb_client.describe_table(TableName=table_name)
    except ClientError as ce:
        if ce.response['Error']['Code'] == 'ResourceNotFoundException':
            return("Table " + table_name + " does not exist.")
        else:
            return("Unknown exception occurred while accessing " + table_name + " table. Full error: " + ce.response)
        
    item_count = table.item_count
    
    if item_count == 0:
        item_count = 100

    keys = []

    for counter in range(0, total_items):
        random_id = secrets.choice(range(1, item_count))
        if (random_id not in keys):
            keys.append(random_id)
        else:
            counter = counter - 1

    response = dynamodb_object.batch_get_item(
        RequestItems={
            table_name: {
                'Keys': [{'id': id} for id in keys]
            }
        }
    )

    items = {}

    print("Starting sorting at {}".format(datetime.now()))

    for key in response.get('Responses', []):
        items = (response['Responses'][key])
        
    for item in items:
        item['id'] = replace_decimals(item['id'])
        
    print("Finished sorting at {}".format(datetime.now()))
        
    return items

start_date = datetime.now()
print("Starting at {}".format(start_date))

response = get_random_names("facebook_data_dj_full", 100)

end_date = datetime.now()
elapsed_time = end_date - start_date

print("Finished at {}".format(end_date))
print("Operation took {}".format(elapsed_time.total_seconds()))
print("Operation took {}".format(elapsed_time))