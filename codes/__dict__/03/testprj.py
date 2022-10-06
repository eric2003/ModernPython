class MyObj():
    def __init__( self, R ):
        self.r = R
        self.s = 2.3
        self.name = 'Chuck Norris'
        self.phone = '+6661'        

obj = MyObj( 1 )
print( "obj.__dict__ =", obj.__dict__ )