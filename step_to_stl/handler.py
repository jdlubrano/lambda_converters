from __future__ import print_function

import json
import os
import pdb
import urllib2
from base64 import b64encode

from aws_s3 import AwsS3
from conversion_error import ConversionError
from step_to_stl import convert

STEP_KEY_PREFIX = 'cad_files/stl/'

def lambda_handler(event, context):
    print('Running lambda_handler...')

    s3_bucket = event.get('s3_bucket')
    s3_object = event.get('s3_object')

    if not s3_bucket:
        raise ConversionError('No s3_bucket provided')

    if not s3_object:
        raise ConversionError('No s3_object provided')

    return convert_from_s3(s3_bucket, s3_object)

def proxy_handler_s3(event, context):
    print('Running proxy_handler_s3...')

    body = json.loads(event['body'])

    print(body)

    bucket = body.get('bucket')
    key = body.get('key')

    if not bucket:
        return bad_request('bucket')

    if not key:
        return bad_request('key')

    result = convert_from_s3(bucket, key)

    return {'statusCode': 201, 'body': json.dumps(result)}

def proxy_handler_url(event, context):
    print('Running proxy_handler_url...')

    body = json.loads(event['body'])

    print(body)

    url = body.get('url')

    if not url:
        return bad_request('url')

    stl_path = convert_from_url(url)

    result = {'base64_stl': encode_file_contents(stl_path)}

    return {'statusCode': 201, 'body': json.dumps(result)}

def bad_request(missing_key):
    body = json.dumps({'message': 'No {} provided'.format(missing_key)})
    return {'statusCode': 400, body: body, 'headers': {'Content-Type': 'application/json'}}

def convert_from_s3(bucket, key):
    local_step = '/tmp/' + os.path.basename(key)

    s3 = AwsS3()

    print('Fetching {}/{} and saving to {}'.format(bucket, key, local_step))

    s3.get_object(bucket, key, local_step)

    stl_file = convert_step_to_stl(local_step)
    s3_key = os.path.basename(stl_file)

    print('Uploading {} to {}/{}'.format(stl_file, bucket, s3_key))
    s3.put_object(stl_file, bucket, s3_key)

    return {'bucket': bucket, 'key': s3_key}

def fetch_step_from_url(url):
    local_step = '/tmp/' + url.split('/')[-1]

    with open(local_step, 'wb') as step:
        for line in urllib2.urlopen(url):
            step.write(line)

    return local_step

def convert_from_url(url):
    local_step = fetch_step_from_url(url)
    return convert_step_to_stl(local_step)

def encode_file_contents(path):
    with open(path) as f:
        return b64encode(f.read())

def convert_step_to_stl(local_step):
    step_filename = os.path.splitext(os.path.basename(local_step))[0]
    stl_path = os.path.join('/tmp', step_filename + '.stl')

    print('Converting {} to {}'.format(local_step, stl_path))
    convert(local_step, stl_path)

    return stl_path
