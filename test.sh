#!/bin/sh

LD_LIBRARY_PATH=lib:$LD_LIBRARY_PATH \
nosetests spec/unittests.py

