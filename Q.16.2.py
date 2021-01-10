import random
arr_len    = 10
arr        = [ None ] * arr_len
insert_elm = 3
for itr_1 in range( 0, arr_len ) :
    arr[ itr_1 ] = random.randint( itr_1 - arr_len, itr_1 + arr_len )
print( arr )

# the c way
head = 0
tail = len( arr ) - 1
while head < tail :
    temp = arr[ head ]
    arr[ head ] = arr[ tail ]
    arr[ tail ] = arr[ head ]
    head = head + 1
    tail = tail - 1
print( arr )

# the python way
print( list( reversed( arr ) ) )
