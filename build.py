#! /usr/bin/python
from __future__ import print_function
import getopt
import os
import pdb
import shutil
import sys

def usage():
    print('''
    Usage: build.py -d <directory>

    Will copy OpenCascade and PythonOCC libraries
    into the given directory.

    See this help message with the option -h.
    ''')
    sys.exit(2)

def build_root():
    return os.path.dirname(os.path.abspath(__file__))

def copy_common_files(build_dir):
    common_files_txt = os.path.join(build_root(), 'common_files.txt')

    with open(common_files_txt) as f:
        for common_file in f:
            common_file = common_file.strip()
            if not common_file: continue

            src = os.path.join(build_root(), common_file)
            dst = os.path.join(build_dir, os.path.basename(common_file))
            print("Copying {} to {}".format(src, dst))
            shutil.copy(src, dst)

def copy_libs(build_dir, libs_src, libs_dst, libs_list):
    if not os.path.isdir(libs_dst):
        os.makedirs(libs_dst)

    with open(libs_list) as f:
        for lib in f:
            lib = lib.strip()
            lib_src = os.path.join(libs_src, lib)
            lib_dst = os.path.join(libs_dst, lib)
            print("Copying {} to {}".format(lib_src, lib_dst))
            shutil.copy(lib_src, lib_dst)


def copy_oce_libs(build_dir):
    libs_src = os.path.join(build_root(), 'oce', 'lib')
    libs_dst = os.path.join(build_dir, 'lib')
    libs_txt = os.path.join(build_dir, 'libs_oce.txt')
    copy_libs(build_dir, libs_src, libs_dst, libs_txt)

def copy_python_libs(build_dir):
    libs_src = os.path.join(build_root(), 'pythonocc', 'lib', 'OCC')
    libs_dst = os.path.join(build_dir, 'OCC')
    libs_txt = os.path.join(build_dir, 'libs_pythonocc.txt')
    copy_libs(build_dir, libs_src, libs_dst, libs_txt)

def build_project(directory):
    print("\nAttempting to build {}".format(directory))

    if not os.path.isdir(directory):
        print("Could not find {}".format(directory))
        return 1

    copy_common_files(directory)
    copy_oce_libs(directory)
    copy_python_libs(directory)

    return 0


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hd:")
    except getopt.GetoptError:
        usage()

    directory = None
    for opt, arg in opts:
        if opt == "-d":
            directory = arg
        if opt == "-h":
            usage()

    ret = 0
    if directory != None:
        ret = build_project(directory)
    else:
        print("\n    Error: No directory given")
        usage()

    print()
    sys.exit(ret)

if __name__ == '__main__':
  main(sys.argv[1:])
