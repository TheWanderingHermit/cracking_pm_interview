arr_len    = 10
arr        = [ None ] * arr_len
insert_elm = 3
for itr_1 in range( 0, arr_len - 1 ) :
    arr[ itr_1 ] = itr_1
insert_at  = arr.index( insert_elm ) + 1

# the c way
for itr_2 in reversed( range( insert_elm, arr_len ) ) :
    arr[ itr_2 ] = arr[ itr_2 - 1 ]
arr[ itr_2 ] = insert_elm
print( arr )

# the python way
print( arr[ 0 : insert_at - 1 ] + [ insert_elm ] + arr[ insert_at : len( arr ) ] )
