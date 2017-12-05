from __future__ import print_function

from base64 import b64encode, b64decode
from conversion_error import ConversionError
from step_to_stl import convert

def convert_base64(event, context):
    print('Running convert_and_download')
    print(event)

    base64step = event.get('base64_step')
    step_path = '/tmp/part.step'
    stl_path = '/tmp/part.stl'

    if not base64step:
        raise ConversionError('No base64_step provided')

    with open(step_path, 'wb') as step:
        step.write(b64decode(base64step))

    convert(step_path, stl_path)

    with open(stl_path) as stl:
        encoded = b64encode(stl.read())
        print(encoded)
        return encoded
