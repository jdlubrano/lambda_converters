#!/bin/sh

LD_LIBRARY_PATH=lib:oce/lib:$LD_LIBRARY_PATH \
PYTHONPATH=pythonocc/lib:$PYTHONPATH \
nosetests tests/unittests.py

