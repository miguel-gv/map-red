
#A variable prevSales sirve para recoller o valor da chave en caso de que exista anteriormente
#O dicionario sirve como hub de todas as relacións chave-valor
import sys;

prevSales = 0
dicto = {}



for line in sys.stdin:
    

    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:

        # Something has gone wrong. Skip this line.

        continue



    thisKey, thisSale = data_mapped

    #Se a key non existe, a crea no dicionario

    if thisKey not in dicto:

        dicto[thisKey] = thisSale 

    #Se a key existe, añádelle o valor das nova venda ao contador anterior
    else:

        prevSales = dicto.get(thisKey)

        dicto.update({'{}'.format(thisKey): float(thisSale) + float(prevSales)})




# Escribe o último par, unha vez rematado o bucle


for i in dicto:
    print('{} --- {}'.format(i, dicto[i]))