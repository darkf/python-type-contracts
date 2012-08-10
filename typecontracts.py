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
#	 # x is ensured to be an int
#	 # y is ensured to be an str
#	 # z is ensured to be an object with the attributes foo (of type Callable)
#		 and bar (of type str)

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

			def rec_typecheck(given, stored):
				if type(given) == types.TupleType:
					if type(stored) == types.TupleType:
						for i in range(len(given)):
							rec_typecheck(given[i], stored[i])
					else:
						raise TypeError("Expected %s but got %s" % (type(stored), type(given)))
				elif type(given) == types.DictType:
					if type(stored) == types.DictType:
						for k in given:
							rec_typecheck(given[k], stored[k])
					else:
						raise TypeError("Expected %s but got %s" % (type(stored), type(given)))
				elif type(given) != stored: # For non-container types
					raise TypeError("Expected %s but got %s" % (stored, type(given)))

			rec_typecheck(tuple(args), tuple(self.annotations))
			return old_f(*args)

		return f
