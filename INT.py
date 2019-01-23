"""
INT(x), though not explained thoroughly in the book, stands for "interchanged" 
and "has to do with eta sequence
More can be found in the paper (ETA-LORE) https://oeis.org/A006336/a006336_1.pdf

This function, whose graphic representation is very peculiar, 
uses the concept of VS sequence and VC sequence of a number
VC: Vertical Coun and Vertical Sep-sequences or an eta-sequence

The nth term of VC is the coun of the nth derivative of eta(alpha),
and the nth term os VS is the sep of the nth derivative of eta(alpha)

The sequences this papers present are infinite sequence composer of 
a finit number of intergers (e.g. 1221121212221....)

This sequences are composer of finite chunks, that will appear in the sequence 
an infinite number of times 
If this chunk are identified by an integer, the "meta-sequence", composed of the 
identifiers of the chunk of the sequence in order, is called the derivative 
of the og sequence (!= calculus derivative)
Eta-sequence can be infinitely differentiable sequences: the derivate of an 
eta-sequence is another eta-sequence!
Eta-sequences are composed of only two consecutive integers

Example:
22121221212212121221212212121 to chunks
221 21 221 21 221 21 21 221 21 221 to ids
2   1   2  1   2  1   1  2   1  2 = the derivative: an eta sequence composed of the same two integers

eta_k (alpha) = [(k-1) alpha]] - [k alpha]
if alpha is pi, eta(alpha) is composed of 3's and 4's
3333334333333343333334
 => to forme the derivative, we need to give integer-names to the chunks 
we can either count the number of 3's in a chunk, or the length of the chunk

Hence the word "coun" : here the 3's, and 'sep' (separator) , here 4's
In genral, the coun will be the closest integer to alpha 

Comming back to the definition:
INT(x) = y, where VC(x) = VS(y) and VS(x) = VC(y),
where the nth elemnt of VC is the coun of the nth derivative of eta(x),
and the nth element of VS is the sep of the nth derivate of eta(x)

The recursion in INT(), which can be seen in its graph, resides in this 
definition:
	INT(alpha) = INT(alpha-N) + N, where N is the integer part of alpha
Thanks to this definition, we can pretty much ignore all the stuff that was said
before; but there is still one problem: This definition is cyclic, not recursive.
We need to define a value which allow the recursion to "bottom out".

In other words, you need to shift alpha in the relevant region of the x-axis 
, that pop in back into the correct part of the y axis, which can be translated as:
INT(alpha) = g(INT(f(alpha)))
where f "shrinks" alpha to the part of the graph you have to look at, and 
g "expands" it back where it belongs.
According to the proof of the paper, f(x) = 1/X, and g(x) = 1/(1-x)

The "box" between N and N+1 is mapped onto a subgraph 
located between 1/N and 1/N+1

Note: this definition only works for alpha > 1, else the integer part 
of alpha = 0, thus INT(alpha) = INT(alpha)
BUT all the information needed are between x=0 and x=1: all the others
value are copies of that box


BACK TO CHUNKS
new style: 211 : chunk_id = 3 (# of #)
old style: 211: chunk_id = 2 (# of coun)

if wze take derivatives in the new style, each term is increased by one (old style - the separator) => the derivate is no longer the eta-sequence of alpha', but of 1+alpha'
1+alpha' = D

1+alpha' = (sep-alpha)/(alpha-coun) + 1

the nth element of VC / VS is equal to the coun/sep of D(D(D...(D(alpha))))) where
the # of D is equal to n

"""

import math
import itertools

depth = 30
phi = (1+math.sqrt(5))/2


def eta(alpha):
	res = []
	sep = coun = None
	coun2 = 9999999999999999999999999
	sep2 = -999999999999999999999999
	for x in range(0,depth):
		res.append(math.floor((x+1)*alpha) - math.floor(x * alpha))
	mx = max(res)
	mn = min(res)
	k_max = max(len(list(y)) for (c,y) in itertools.groupby(res) if c==mx)
	k_min = max(len(list(y)) for (c,y) in itertools.groupby(res) if c==mn)
	if k_max == 1:
		return mx,mn
	else:
		return mn,mx
		

def D(a):
	sep,coun = eta(a)
	if a-coun == 0:
		return None
	return (sep - a)/(a-coun) + 1



def vc_vs(a):
	alphas = []
	alphas.append(a)
	vc = []
	vs = []
	og_sep, og_coun = eta(alphas[0])
	vc.append(og_coun)
	vs.append(og_sep)
	for x in range(0,10):
		a = D(alphas[-1])
		if a == None:
			return None,None
		alphas.append(a)
		new_vs, new_vc = eta(a)
		vc.append(new_vc)
		vs.append(new_vs)
	return vc,vs

rootc,roots = vc_vs(math.sqrt(2))
phic,phis = vc_vs(phi)

print(rootc)
print(roots)
print(phic)
print(phis)

testc,tests = vc_vs(0.30161899999995667)
testc2,tests2 = vc_vs(0.5112569999949725)

print(testc)
print(tests)
print(testc2)
print(tests2)

#sys.exit(0)

#all_vc [rootc,phic]
#all_vs = [roots,phis]

all_vc = {}
all_vs = {}

hashes_vc = {}
hashes_vs = {}

with open("test", 'w') as f:
	
	i = 0.3
	while i < 0.7:
		#print(i)
		vc,vs = vc_vs(i)
		if vc is None or vs is None:
			i += 0.000001
			continue
		all_vc[i]=vc
		all_vs[i]=vs
		hashes_vs[i] = hash(set(vs))
		hashes_vc[i] = hash(set(vc))
		i += 0.000001


def lst_eq(a,b):
	for i in range(0,len(a)):
		if a[i] != b[i]:
			return False
	return True

print(all_vc)
print(all_vs)

print("Comparison")
for x in hashes_vc.keys():
	found = False
	for y in reversed(list(hashes_vs.keys())):
		if hashes_vc[x] == hashes_vs[y] and hashes_vs[x] == hasehs_vc[y]:
			print("wow")



for x in all_vc.keys():
	found = False
	for y in reversed(list(all_vs.keys())):
		if lst_eq(all_vc[x],all_vs[y]):
			print("{},{}".format(x,y))
			found = True
		if found:
			break
