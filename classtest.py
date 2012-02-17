from typecontracts import contract

class Foo:
  def __init__(self, x):
    self.x = x
    
class Bar:
  pass
    
@contract(Foo)
def func(x):
  print x.x

func(Foo(5)) # should pass
func(Bar())  # should fail