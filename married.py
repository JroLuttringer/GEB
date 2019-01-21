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
