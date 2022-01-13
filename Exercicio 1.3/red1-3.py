#!/usr/bin/python3



import sys

#Variable que recolle o último máximo e un dicionario vacío onde meteremos todos os valores

prevMax = 0
dicto = {}



for line in sys.stdin:

    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:

        # Something has gone wrong. Skip this line.

        continue



    thisKey, thisSale = data_mapped


    #Se a chave non existe no dicionario, engadímosela. Se existe, comprobamos o valor
    #antigo co novo, e en caso de que o supere a actualizamos

    if thisKey not in dicto:

        dicto[thisKey] = thisSale
    
    else:
        prevMax = dicto.get(thisKey)
        if float(prevMax) < float(thisSale):
           dicto.update({'{}'.format(thisKey) : float(thisSale)})

    oldKey = thisKey



# Imprimimos o par chave : valor máximo

for i in dicto:

    print('{} --- {}'.format(i, dicto[i]))
