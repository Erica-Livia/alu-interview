#!/usr/bin/python3
"""minOperation"""
from math import sqrt


def minOperations(n):
	if n <= 1:
		return 0
	
	for i in ranfe(2, n+1):
		if n % i == 0:
			factor = n // i
