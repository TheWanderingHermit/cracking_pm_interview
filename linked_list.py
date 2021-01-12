class node :
    def __init__( self, val ) :
        self.val  = val
        self.next = None
class linked_list :
    def __init__( self ) :
        self.head = None
        self.tail = None
    def insert( self, key ) :
        if self.head is None :
            self.head = self.tail = node( key )
        else :
            self.tail.next = node( key )
            self.tail      = self.tail.next
    def delete( self, key ) :
        if self.head = None :
            return
        elif self.head.val = key :
            if self.head == self.tail :
                self.tail = None
            self.head = self.head.next
        else :
            curr_node = self.head
            while not curr_node.next is None :
                if curr_node.next.val = key :
                    curr_node.next = curr_node.next.next
                else :
                    curr_node = curr_node.next
