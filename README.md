# Lambda Converters

A project containing several AWS Lambda file converters.

## Building Lambda Functions

### Underlying Technologies

These lambda functions depend heavily on the
[Open Cascade Community Edition](https://github.com/tpaviot/oce) and
[PythonOCC](http://www.pythonocc.org).

### Environment

This project contains pre-compiled binaries in `oce` and `pythonocc`.  These
binaries were compiled on an AWS Linux instance, but they also run on
Ubuntu 16.04.

You will have trouble if you try to use these binaries on a Mac.
Unfortunately, there is currently no solution for compiling PythonOCC libraries
from source on an OSX machine (at least in my experience).

### build.py

The `build.py` script is meant to automate the build process for these
lambda functions.  You can rebuild a particular lambda by running
`./build.py -d <lambda_directory>`.  The build script expects to find two files
within a lambda's directory.

  - libs_oce.txt - a list of OpenCascade libraries to copy into the lambda's
                   `lib` directory.

  - libs_pythonocc.txt - a list of PythonOCC libraries to copy into the lambda's
                         `OCC` directory.

The build script will also copy the files listed in `common_files.txt` into
the root of the lambda's directory.

## Tests

See the `step_to_stl` directory as an example.  It helps
to have a `test.sh` script in the lambda's root directory
so that the `LD_LIBRARY_PATH` environment variable can be
set before running any unit tests.

## Troubleshooting

If you see
```
TypeError: in method 'StlAPI_Writer_Write', argument 3 of type 'char const *'
```

or something complaining about `char const *` arguments, these are a result
of using SWIG with OpenCascade.  To fix such an issue, pass your string-like
objects to PythonOCC functions using Python's `str` function.

Example:
```python
status = step_reader.ReadFile(str(filename))
```

## Rebuilding Binaries

The following steps took place on an AWS EC2 instance
running AWS Linux.

The steps below assume that the project will be built at
`/home/ec2-user/lambda_converters`.

#### Copy libGLU

AWS Lambda functions' runtime environment does not contain libGLU, so we
need to provide a copy of it.

Find libGLU.so somewhere on your system (or install it, then find it) and
copy it `/home/ec2-user/lambda_converters/lib`.

#### Compile OCE
```
cd /home/ec2-user/lambda_converters
git clone git@github.com:tpaviot/oce.git
cd oce
git fetch origin
git checkout -b 0.16.1 origin/OCE-0.16.1
mkdir build && cd build
cmake -DOCE_INSTALL_PREFIX=/home/ec2-user/lambda_converters/oce ..
make
make install/strip
```

#### Compile Python OCC

**Install Dependencies**
```
sudo yum install swig
```

**Install PythonOCC Core**
```
cd /home/ec2-user/lambda_converters
git clone git://github.com/tpaviot/pythonocc-core.git pythonocc
cd pythonocc
mkdir cmake-build && cd cmake-build
cmake -DOCE_INCLUDE_PATH=/home/ec2-user/lambda_converters/oce/include/oce \
-DOCE_LIB_PATH=/home/ec2-user/lambda_converters/oce/lib ..
make
```
