import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PedidosCafe')

def lambda_handler(event, context):

    body = json.loads(event['body'])

    pedido_id = str(uuid.uuid4())

    item = {
        'pedidoId': pedido_id,
        'cliente': body['cliente'],
        'cafe': body['cafe']
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'mensaje': 'Pedido registrado correctamente',
            'pedidoId': pedido_id
        })
    }