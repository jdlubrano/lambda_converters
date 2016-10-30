#!/bin/sh

# Creates a zip file that can be deployed as an AWS Lambda function

zip -r9 step_to_stl_lambda.zip \
aws_s3.py \
conversion_error.py \
handler.py \
step_to_stl.py \
lib \
OCC/*.py \
OCC/*.so
