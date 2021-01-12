import bin_search_tree

bst = bin_search_tree.bin_search_tree()
bst.insert( 2 )
bst.print_tree()
print("\n")
bst.insert( 6 )
bst.print_tree()
print("\n")
bst.insert( 10 )
bst.print_tree()
print("\n")
bst.insert( -20 )
bst.print_tree()
print("\n")
# still a bug in delete
print( bst.delete( -20 ) )
bst.print_tree()
print("\n")
