

def fibo(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)



def lucas(n):
	if n == 1:
		return 1
	if n == 2:
		return 3
	else:
		return lucas(n-1) + lucas(n-2)



depth = 10
for x in range(1, depth):
	print("{} {}".format(fibo(x), lucas(x)))
