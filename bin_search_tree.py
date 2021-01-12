class node :
    def __init__( self, key ) :
        self.l_child = None
        self.r_child = None
        self.val     = key

class bin_search_tree :
    def __init__( self ) :
        self.root = None
    def insert( self, key ) :
        if self.root is None :
            self.root = node( key )
        else :
            return self.insert_helper( self.root, key )
    def insert_helper( self, root, key ) :
        if root.val > key :
            if root.l_child is None :
                root.l_child = node( key )
            else :
                self.insert_helper( root.l_child, key )
        elif root.val < key :
            if root.r_child is None :
                root.r_child = node( key )
            else :
                self.insert_helper( root.r_child, key )
        else :
            return False
        return True
    def min_val( self, root ) :
        t_node = root
        while not t_node.l_child is None :
            t_node = t_node.l_child
        return t_node
    def print_tree( self ) :
        self.print_tree_helper( self.root )
    def print_tree_helper( self, root ) :
        if not root :
            return
        self.print_tree_helper( root.l_child )
        print( root.val )
        self.print_tree_helper( root.r_child )
    def delete( self, key ) :
        return self.delete_helper( self.root, key )
    def delete_helper( self, root, key ) :
        if root is None :
            return False
        if root.val > key :
            self.delete_helper( root.l_child, key )
        elif root.val < key :
            self.delete_helper( root.r_child, key )
        else :
            if root.l_child is None :
                root = root.r_child
            elif root.r_child is None :
                root = root.l_child
            else :
                root = min_val( root )
        return True
