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

obj = MyObj(1)
print( "obj.__dict__ =", obj.__dict__ )

print( "dir( obj ) =", dir( obj ) )

#print( "obj.strange_name =", obj.strange_name )
obj.foo_haha()
print( "obj.strange_name =", obj.strange_name )
print( "obj.__dict__ =", obj.__dict__ )
print( "dir( obj ) =", dir( obj ) )
