from __future__ import print_function

import json
import os
import re

from aws_s3 import AwsS3
from conversion_error import ConversionError
from step_to_stl import convert

def stl_key(step_object):
    dest = re.sub(r'/(stp|step)/', '/stl/', step_object)
    return os.path.splitext(dest)[0] + '.stl'

def lambda_handler(event, context):
    print('Running lambda_handler...')

    s3_bucket = event.get('s3_bucket')
    s3_object = event.get('s3_object')

    if not s3_bucket:
        raise ConversionError('No s3_bucket provided')

    if not s3_object:
        raise ConversionError('No s3_object provided')

    local_step = '/tmp/' + os.path.basename(s3_object)

    s3 = AwsS3()

    print('Fetching {}/{} and saving to {}'.format(s3_bucket,
                                                   s3_object,
                                                   local_step))

    s3.get_object(s3_bucket, s3_object, local_step)

    stl_file = os.path.splitext(local_step)[0] + '.stl'

    print('Converting {} to {}'.format(local_step, stl_file))
    convert(local_step, stl_file)

    s3_key = stl_key(s3_object)

    print('Uploading {} to {}/{}'.format(stl_file, s3_bucket, s3_key))
    s3.put_object(stl_file, s3_bucket, s3_key)
