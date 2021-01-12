import stack

curr_stack = stack.stack( 5 )
curr_stack.push( 4 )
curr_stack.push( 3 )
curr_stack.push( 6 )
curr_stack.push( 1 )
curr_stack.push( 8 )
curr_stack.print_stack()
print("\n")

def reverse_stack( parent_stack ) :
    reversed_stack = stack.stack( 5 )
    while parent_stack.peek() :
        reversed_stack.push( parent_stack.pop() )
    return reversed_stack

reverse_stack( curr_stack ).print_stack()
