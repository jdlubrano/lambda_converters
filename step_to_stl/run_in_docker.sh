#!/bin/sh

docker run -v "$PWD":/var/task -it --rm lambci/lambda:build-python2.7 bash
