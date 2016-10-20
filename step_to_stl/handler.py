# import boto3
import json
import os
import subprocess

from s3_file_retriever import get_s3_file

import lambda_env

def lambda_handler(event, context):
    print 'Running lambda_handler...'

    s3_bucket = event.get('s3_bucket')
    s3_object = event.get('s3_object')

    if not cad_file_url:
        return { 'error': 'No cad_file_url provided' }

    result = get_s3_file(s3_bucket, s3_object)

    command = ' '.join([
        lambda_env.ld_library_path(),
        lambda_env.python_path(),
        'python',
        'step_to_stl.py',
        '-i',
        result.get('filepath'),
        '-o',

    ])

    print 'Running %s' % command

    output = subprocess.check_output(command,
                                     stderr=subprocess.STDOUT,
                                     shell=True)

    print output
    return { 'message': output.splitlines()[-1] }
