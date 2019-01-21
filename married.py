"""
The married functions are often different at first
i.e., at the begin, when x is small, f[x] and m[x] do not return the same value 
as time goes on and x increases, f and m return the same value for longer periods of time 

In fact, the number of time they are equal to each other before diverging follows the fibonacci sequence 
f and m returns the same result 1 times before not having the same result, than 1 , than 2, than 3, than 5, than 8 ....

Said in another fashion, F & M differ at iteration 0, 1, 2, 4, 7, 12
1-0 = 1
2-1 = 1
4-2 = 2
7-4 = 3
12-7 = 5

Said in ANOTHER way, F[n] != M[n] if n+1 is in the fibonacci sequence

"""


depth = 100

_f = []
_m = []

def m(n):
	if n == 0:
		return 0
	else:
		return n - f(m(n-1))

def f(n):
	if n == 0:
		return 1
	else:
		return n - m(f(n-1))


for x in range(0, depth):
	_f.append(f(x))
	_m.append(m(x))


print("F: {}".format(_f))
print("M: {}".format(_m))

i = 0 
last_difference_index = 0
for x in _f:
	if _f[i] != _m[i]:
		print("F and M are different at index {} - They were egal to each other for {} iterations".format(i, i-last_difference_index))
		last_difference_index = i
	i += 1
