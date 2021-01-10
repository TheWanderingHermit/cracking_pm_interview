sales = [ [ 211, 4 ],
          [ 262, 3 ],
          [ 211, 5 ],
          [ 216, 6 ] ]

def get_total_sales( sales ) :
    total_sales_dict = dict()
    for sale in sales :
        total_sales_dict.setdefault( sale[ 0 ], 0 )
        total_sales_dict[ sale[ 0 ] ] = total_sales_dict[ sale[ 0 ] ] + sale[ 1 ]
    total_sales_list = list()
    for sale_id in total_sales_dict :
        total_sales_list.append( [ sale_id, total_sales_dict[ sale_id ] ] )
    return total_sales_list
print( get_total_sales( sales ) )
