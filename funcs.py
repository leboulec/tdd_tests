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
	moyenne = float(sum(l)/len(l))
	return moyenne

def ecart_type_int(list):
	return -1
