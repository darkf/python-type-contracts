from typecontracts import contract

@contract((int, str))
def foo(t):
  print "t0:", t[0] 
  print "t1:", t[1]

@contract({"foo": str, "bar": int})
def bar(d):
 print "d0:", d['foo']
 print "d1:", d['bar']

try:
	foo((5, "hi"))  # should pass
except:
	print "Test #1 failed"

try:
	foo(("9", 666)) # should fail
except:
	print "Test #2 failed"

try:
	bar({"foo": "hello", "bar": 5})
except:
	print "Test #3 failed"

try:
	bar({"foo": 5, "bar": "hello"})
except:
	print "Test #4 failed"
