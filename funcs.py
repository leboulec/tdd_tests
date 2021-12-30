# coding=utf-8
import math

def max_int(a,b):
	if a < b :
		return b
	else :
		return a

def min_int(a,b):
    if a < b:
        return a
    else:
        return b

""" La médiane renvoit la valeur basse
"""
def mediane_int(l):
	if (l == []):
		return None
	tmp = l
	tmp.sort()
	lon = len(tmp)
	if lon % 2 == 0:
		return tmp[len(tmp) // 2 - 1]
	else:
		return tmp[len(tmp) // 2]

def moyenne_int(l):
	moyenne = sum(l)/float(len(l))
	return moyenne

def ecart_type_int(list):
	if (list == []):
		return None

	mean = sum(list) / len(list)
	var = sum((l-mean)**2 for l in list) / len(list)
	st_dev = math.sqrt(var)

	return st_dev

def is_geometric(li):
	return -1
