import os

def cwd():
    return os.path.dirname(os.path.abspath(__file__))

def ld_library_path():
    return 'LD_LIBRARY_PATH='
        + cwd()
        + '/oce/lib:'
        + os.environ['LD_LIBRARY_PATH']

def python_path():
    return 'PYTHONPATH='
        + cwd()
        + '/pythonocc/lib:'
        + os.environ['PYTHONPATH']
