import random

random.seed()
length_1 = 5
length_2 = 10
arr_1    = [ None ] * length_1
arr_2    = [ None ] * length_2
for itr_1 in range( 0, len( arr_1 ) ) :
    arr_1[ itr_1 ] = random.randint( 0, itr_1 )
for itr_2 in range( 0, len( arr_2 ) ) :
    arr_2[ itr_2 ] = random.randint( 0, itr_2 )
print( arr_1 )
print( arr_2 )

# the c way
dictionary_1 = { x : 0 for x in arr_1 }
dictionary_2 = { y : 0 for y in arr_2 }
def is_subset( dictionary_1, dictionary_2 ) :
    for elem in dictionary_1 :
        if elem not in dictionary_2 :
            return False
    return True
print( is_subset( dictionary_1, dictionary_2 ) )

# the python way
print( set( arr_1 ).issubset( set( arr_2 ) ) )
