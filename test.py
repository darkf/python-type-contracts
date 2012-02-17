from typecontracts import contract

@contract(int, str)
def foo(x, y):
  print "x:", x
  print "y:", y

foo(5, "hi")  # should pass
foo("9", 666) # should fail