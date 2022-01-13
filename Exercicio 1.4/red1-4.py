#!/usr/bin/python3



import sys


thisSale = 0.0

saleMax = 0.0

oldKey = None





for line in sys.stdin:

    thisSale = float(line)

    #Co comprobador do anterior máximo, comprobamos liña por liña e o actualizamos se a nova liña é maior
    
    if thisSale > saleMax:
       saleMax = thisSale


print('A venda máxima é de {}'.format(saleMax))