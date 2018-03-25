import utils


def foo(n):
	iterationNumber = 0
	while not utils.isPalindrom(n):
		n += int(str(n)[:: -1])
		iterationNumber += 1
	print(iterationNumber)


foo(196)
