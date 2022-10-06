class MyObj():
    abcd = "haha"
    def __init__( self, R ):
        self.r = R
        self.s = 2.3
    def myfun():
        pass

obj = MyObj(1)
print( "obj.__dict__ =", obj.__dict__ )

print( "dir( obj ) =", dir( obj ) )