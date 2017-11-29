from __future__ import print_function

import getopt
import os
import pdb
import sys

from conversion_error import ConversionError

from OCC.StlAPI import StlAPI_Writer
from OCC.STEPControl import STEPControl_Reader
from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity

def usage():
    print('step_to_stl.py -i source -o dest')
    sys.exit(2)

def get_shape_from_file(filename):
    step_reader = STEPControl_Reader()
    status = step_reader.ReadFile(str(filename))

    if status == IFSelect_RetDone:
        number_of_roots = step_reader.NbRootsForTransfer()
    else:
        raise ConversionError("Could not read {}".format(filename))

    i = 1
    ok = False
    while not ok and i <= number_of_roots:
        ok = step_reader.TransferRoot(i)
        i += 1

    return ok and step_reader.Shape(1)

def convert(source, dest):
    output = os.path.abspath(dest)
    shape = get_shape_from_file(source)

    if not shape:
        raise ConversionError("Could not create {}".format(output))

    stl_ascii = False
    stl_writer = StlAPI_Writer()
    stl_writer.SetASCIIMode(stl_ascii)
    stl_writer.Write(shape, str(output))
    return output

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["infile=", "outfile="])
    except getopt.GetoptError:
        usage()

    source = None
    dest = None
    for opt, arg in opts:
        if opt in ("-i", "--infile"):
            source = arg
        if opt in ("-o", "--outfile"):
            dest = arg
        if opt in ("-h"):
            usage()

    if source != None and dest != None:
        output = convert(source, dest)
        print("STL File: {}".format(output))
    else:
        usage()

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])

