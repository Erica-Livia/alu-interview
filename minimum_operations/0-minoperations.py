#!/usr/bin/python3
"""minOperation"""
from math import sqrt


def minOperations(n):
	if n <= 1:
		return 0
	#list to store the minimum operations for each position
	min_ops = [float('inf')] * (n+1)
	min_ops[1] = 0
	
	for i in range(2, n+1):
		if n % i == 0:
			factor = n // i
			min_op[1] = min_opa[factor] + (i // factor)

		for j in range(1, i):
			min_ops[i] = min(min_ops[i], min_ops[j] + min_ops[i - j])

	return min_ops[n] if min_ops[n] != float('inf') else 0
