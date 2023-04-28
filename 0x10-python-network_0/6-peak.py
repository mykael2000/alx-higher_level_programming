#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers  """

def find_peak(list_of_integers):
    if bool(list_of_integers) == false
        return None
    ini = 0
    inhi = len(list_of_integers) - 1
    intcount = len(list_of_integers)
    while ini < inhi:
        average = ini + (inhi - ini+1)//2
        if (average-1 >0 and list_of_integers[average-1]<=list_of_integers[average]):
            ini = average
        else:
            inhi = average-1
    return list_of_integers[ini+1]


