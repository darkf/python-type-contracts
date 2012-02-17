# Type Contracts v0.1
# Copyright (c) 2012 darkf
# Licensed under the terms of the MIT license
#
# This library implements very simple dynamic type-checking
# which I call "type contracts".
# Basically it allows you to do this:
#
# @contract(int, str, {"foo": Callable, "bar": str})
# def func(x, y, z):
#   # x is ensured to be an int
#   # y is ensured to be an str
#   # z is ensured to be an object with the attributes foo (of type Callable)
#     and bar (of type str)

# todo: object typechecking and keyword arguments
import types

class contract:
  def __init__(self, *annotations):
    self.annotations = annotations
    
  def __call__(self, old_f, *args):
    # simple type-checking

    def f(*args):    
      if len(args) != len(self.annotations):
        raise TypeError("Expected %d arguments, got %d" % (len(self.annotations), len(args)))
      
      for i,a in enumerate(self.annotations):
        if type(a) == types.ClassType:
          if not isinstance(args[i], a):
            raise TypeError("Argument %d: expected instance of %s, got %s" % (i+1, a, type(args[i])))
        
        elif type(a) == dict or type(a) == object:
          raise NotImplementedError("object typechecking is not implemented yet")
          
        elif type(args[i]) != a:
          raise TypeError("Argument %d: expected an %s, got an %s" % (i+1, a, type(args[i])))
          
      return old_f(*args)
        
    return f