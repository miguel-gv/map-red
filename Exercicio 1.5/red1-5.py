#!/usr/bin/python3



import sys





saleTotal = 0.0

oldKey = None



# Loop around the data

# It will be in the format key\tval

# Where key is the store name, val is the sale amount

#

# All the sales for a particular store will be presented,

# then the key will change and we'll be dealing with the next store



for line in sys.stdin:



    

    saleTotal += float(line)







print('As vendas totales son de {}'.format(saleTotal))