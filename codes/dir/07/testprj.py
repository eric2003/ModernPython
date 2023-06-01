class MyObj():
    abcd = "haha"
    def __init__( self, R ):
        self.r = R
        self.s = 2.3
    def myfun():
        pass
    def foo_haha( self ):
        self.strange_name = "strange"
        print( "self.strange_name =", self.strange_name )        

print( "MyObj.__dict__ =", MyObj.__dict__ )

print( "dir( MyObj ) =", dir( MyObj ) )

obj = MyObj(1)

print( "MyObj.__dict__ =", MyObj.__dict__ )

print( "dir( MyObj ) =", dir( MyObj ) )

