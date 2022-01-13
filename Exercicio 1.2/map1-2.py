#!/usr/bin/python3

import sys

#Collemos Item e Cost para o reducer

for line in sys.stdin:

    data = line.strip().split("\t")

    if (len(data) != 6):

       continue

    date, time, store, item, cost, payment = data

    print(f'{item}\t{cost}')