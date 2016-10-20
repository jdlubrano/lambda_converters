# import boto3
import json
import os
import subprocess

from cad_retriever import get_cad_file

print 'Loading...'

def lambda_handler(event, context):
  print 'Running lambda_handler...'

  cad_file_url = event.get('cad_file_url')

  if not cad_file_url:
    return { 'error': 'No cad_file_url provided' }

  result = get_cad_file(cad_file_url)

  if result.get('error'): return result

  cwd = os.path.dirname(os.path.abspath(__file__))
 
  command = ' '.join([
    'LD_LIBRARY_PATH=' + cwd + '/oce/lib:' + os.environ['LD_LIBRARY_PATH'],
    'PYTHONPATH=' + cwd + '/pythonocc/lib:' + os.environ['PYTHONPATH'],
    'python',
    'geometry.py',
    '-f',
    result.get('cad_file')
  ])

  try:
    print 'Running %s' % command
    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    print output
    return json.loads(output.splitlines()[-1])
  except subprocess.CalledProcessError, e:
    print e.output 
    return { 'error': 'Something went wrong with the file analyzer script' }
  except ValueError, e:
    print e
    return { 'error': 'The file analyzer script did not return JSON' }

