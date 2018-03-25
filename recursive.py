import utils

import sys
sys.setrecursionlimit(10000)


def foo(n, iterationNumber):
	if utils.isPalindrom(n):
		print(iterationNumber)
	return foo(n + int(str(n)[:: -1]), iterationNumber + 1)


foo(196, 0)


def foo(n):
	iterationNumber = 0
	while not utils.isPalindrom(n):
		n += int(str(n)[:: -1])
		iterationNumber += 1
	print(iterationNumber)

foo(196)
