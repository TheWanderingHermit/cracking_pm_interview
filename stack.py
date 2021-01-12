class stack :
    def __init__( self, size ) :
        self.size  = size
        self.top   = -1
        self.stack = [ None ] * size
    def peek( self ) :
        return self.stack[ self.top ]
    def push( self, key ) :
        if self.top == self.size - 1:
            return False
        else :
            self.top = self.top + 1
            self.stack[ self.top ] = key
        return True
    def pop( self ) :
        if self.top < 0 :
            return None
        else :
            val = self.stack[ self.top ]
            self.top = self.top - 1
            return val
    def print_stack( self ) :
        print( self.stack )
