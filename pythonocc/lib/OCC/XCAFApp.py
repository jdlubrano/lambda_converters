# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _XCAFApp.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_XCAFApp', [dirname(__file__)])
        except ImportError:
            import _XCAFApp
            return _XCAFApp
        if fp is not None:
            try:
                _mod = imp.load_module('_XCAFApp', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _XCAFApp = swig_import_helper()
    del swig_import_helper
else:
    import _XCAFApp
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _XCAFApp.delete_SwigPyIterator
    def __iter__(self): return self
SwigPyIterator.value = new_instancemethod(_XCAFApp.SwigPyIterator_value,None,SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_XCAFApp.SwigPyIterator_incr,None,SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_XCAFApp.SwigPyIterator_decr,None,SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_XCAFApp.SwigPyIterator_distance,None,SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_XCAFApp.SwigPyIterator_equal,None,SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_XCAFApp.SwigPyIterator_copy,None,SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_XCAFApp.SwigPyIterator_next,None,SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_XCAFApp.SwigPyIterator___next__,None,SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_XCAFApp.SwigPyIterator_previous,None,SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_XCAFApp.SwigPyIterator_advance,None,SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_XCAFApp.SwigPyIterator___eq__,None,SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_XCAFApp.SwigPyIterator___ne__,None,SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_XCAFApp.SwigPyIterator___iadd__,None,SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_XCAFApp.SwigPyIterator___isub__,None,SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_XCAFApp.SwigPyIterator___add__,None,SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_XCAFApp.SwigPyIterator___sub__,None,SwigPyIterator)
SwigPyIterator_swigregister = _XCAFApp.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.TDocStd
import OCC.TDF
import OCC.Standard
import OCC.TCollection
import OCC.MMgt
import OCC.TColStd
import OCC.Resource
def register_handle(handle, base_object):
    """
    Inserts the handle into the base object to
    prevent memory corruption in certain cases
    """
    try:
        if base_object.IsKind("Standard_Transient"):
            base_object.thisHandle = handle
            base_object.thisown = False
    except:
        pass

class XCAFApp_Application(OCC.TDocStd.TDocStd_Application):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def GetApplication(*args):
        """
        * Initializes (for the first time) and returns the static object (XCAFApp_Application) This is the only valid method to get XCAFApp_Application object, and it should be called at least once before any actions with documents in order to init application

        :rtype: Handle_XCAFApp_Application

        """
        return _XCAFApp.XCAFApp_Application_GetApplication(*args)

    GetApplication = staticmethod(GetApplication)
    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_XCAFApp_Application(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _XCAFApp.delete_XCAFApp_Application
XCAFApp_Application_swigregister = _XCAFApp.XCAFApp_Application_swigregister
XCAFApp_Application_swigregister(XCAFApp_Application)

def XCAFApp_Application_GetApplication(*args):
  """
    * Initializes (for the first time) and returns the static object (XCAFApp_Application) This is the only valid method to get XCAFApp_Application object, and it should be called at least once before any actions with documents in order to init application

    :rtype: Handle_XCAFApp_Application

    """
  return _XCAFApp.XCAFApp_Application_GetApplication(*args)

class Handle_XCAFApp_Application(OCC.TDocStd.Handle_TDocStd_Application):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        _XCAFApp.Handle_XCAFApp_Application_swiginit(self,_XCAFApp.new_Handle_XCAFApp_Application(*args))
        # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_XCAFApp.Handle_XCAFApp_Application_DownCast)
    __swig_destroy__ = _XCAFApp.delete_Handle_XCAFApp_Application
Handle_XCAFApp_Application.Nullify = new_instancemethod(_XCAFApp.Handle_XCAFApp_Application_Nullify,None,Handle_XCAFApp_Application)
Handle_XCAFApp_Application.IsNull = new_instancemethod(_XCAFApp.Handle_XCAFApp_Application_IsNull,None,Handle_XCAFApp_Application)
Handle_XCAFApp_Application.GetObject = new_instancemethod(_XCAFApp.Handle_XCAFApp_Application_GetObject,None,Handle_XCAFApp_Application)
Handle_XCAFApp_Application_swigregister = _XCAFApp.Handle_XCAFApp_Application_swigregister
Handle_XCAFApp_Application_swigregister(Handle_XCAFApp_Application)

def Handle_XCAFApp_Application_DownCast(*args):
  return _XCAFApp.Handle_XCAFApp_Application_DownCast(*args)
Handle_XCAFApp_Application_DownCast = _XCAFApp.Handle_XCAFApp_Application_DownCast



