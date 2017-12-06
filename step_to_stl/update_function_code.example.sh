#!/bin/sh

aws lambda update-function-code \
  --function-name stepToStlViaUrl \
  --s3-bucket maketime-lambda \
  --s3-key step_to_stl_lambda.zip
