class MyObj():
    def __init__( self, R ):
        self.r = R
        self.s = 2.3

obj = MyObj( 1 )
print( "obj.__dict__ =", obj.__dict__ )