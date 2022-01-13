#!/usr/bin/python3



import sys


thisSale = 0.0

saleMax = 0.0

oldKey = None





for line in sys.stdin:


    

    thisSale = float(line)


    if thisSale > saleMax:
       saleMax = thisSale

    # Escribe un par key:value ante un cambio na key

    # Reinicia o total

    



print('A venda máxima é de {}'.format(saleMax))