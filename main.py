# 0 1 1 2 3 5 8 13 ...
def fib(n):
	if n < 0:
		return None
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(-3, 10)])