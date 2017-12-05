from __future__ import print_function

import json
from base64 import b64encode, b64decode
from conversion_error import ConversionError
from step_to_stl import convert

def convert_base64(event, context):
    print('Running convert_and_download')
    print(event)

    body = json.loads(event['body'])
    base64step = body.get('base64_step')

    if not base64step:
        return {
                   'statusCode': 400,
                   'body': json.dumps({'message': 'No base64_step provided'}),
                   'headers': {
                       'Content-Type': 'application/json'
                   }
               }

    step_path = '/tmp/part.step'
    with open(step_path, 'wb') as step:
        step.write(b64decode(base64step))

    stl_path = '/tmp/part.stl'
    convert(step_path, stl_path)

    with open(stl_path) as stl:
        return {
                   'statusCode': 201,
                   'body': json.dumps({'base64_stl': b64encode(stl.read())}),
                   'headers': {
                       'Content-Type': 'application/json'
                   }
               }
