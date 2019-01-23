import matplotlib.pyplot as plt 



result=[]
for x in range(0,100000):
	result.append(float("1."+ str(x)))

plt.plot(result)
plt.ylabel("1,x")
plt.show()
