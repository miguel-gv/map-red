#!/usr/bin/python3

import sys

saleTotal = 0.0

for line in sys.stdin:
    
    #Como non necesitamos comprobante, sumamos indiferentemente os datos.

    saleTotal += float(line)

print('As vendas totales son de {}'.format(saleTotal))