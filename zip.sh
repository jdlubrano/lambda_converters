#!/bin/sh

# A template for creating AWS Lambda zip deployment packages

zip -r9 step_geometry_lambda.zip \
aws_s3.py \
conversion_error.py \
handler.py \
lib \
OCC/*.py \
OCC/*.so
