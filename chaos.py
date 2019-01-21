"""
A recursion than seems to generate chaos from a simple definition

"""

def chaos(n):
	if n == 1 or n == 2 :
		return 1
	else:
		return chaos(n-chaos(n-1)) + chaos(n-chaos(n-2))


depth = 50
previous = 0
for x in range(1, depth):
	_chaos = chaos(x)
	print("{} ({})".format(_chaos, _chaos-previous))
	previous = _chaos
