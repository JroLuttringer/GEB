import pygame
import sys
import math
# if you construct a tree by placing G(n) below n, for all values of n, 
# you create diagram G
# meaning that the node whose id is G(n) is a parent of n

# same definition goes for H 

def G(n):
	if n == 0:
		return 0
	return n - G(G(n-1))

def H(n):
	if n == 0:
		return 0
	return n - H(H(H(n-1)))


WIDTH = 3000
HEIGHT = 1500
G_graph = {}
og_pos = (int(WIDTH/2), HEIGHT - 10)



for x in range(0,30):
	parent = G(x)
	if parent == x:
		continue
	if parent not in G_graph.keys():
		G_graph[parent] = []
	G_graph[parent].append(x)

print(G_graph)

def fibo(x):
	if x == 1 or x == 2:
		return 1
	return fibo(x-1) + fibo(x-2)


def fibo_depth(x):
	max_node = 1
	i = 1
	while max_node < x:
		max_node += fibo(i)
		i+=1
	return i



pos = {}
pos[1] = og_pos

for node in G_graph.keys():
	node_x = og_pos[0]
	node_y = og_pos[1]
	for p in G_graph.keys():
		if node in G_graph[p]:
			if len(G_graph[p]) > 1:
				node_y = pos[p][1] - 150
				depth = fibo_depth(node) -3
				if node  == min(G_graph[p]):
					node_x = pos[p][0] - og_pos[0]/math.pow(2,depth)
				else:
					node_x = pos[p][0] + og_pos[0]/math.pow(2,depth)
				
			else:	
				node_x = pos[p][0]
				node_y = pos[p][1] - 150
			pos[node] = (int(node_x), int(node_y))

pygame.init()
pywindow = pygame.display.set_mode((WIDTH, HEIGHT))
pywindow.fill((255,255,255))

print(pos)

for x in range(HEIGHT-10, 0, -150):
	pygame.draw.line(pywindow, (0,0,255), (0,x), (WIDTH,x), 2)
	
myfont = pygame.font.SysFont("Arial", 25)
for x in pos.keys():
	pygame.draw.circle(pywindow, (255,0,0), pos[x], 20,20)
	label = myfont.render(str(x), 50, (0,0,0))
	pywindow.blit(label, (pos[x][0]-10, pos[x][1]-10))

for x in G_graph.keys():
	for child in G_graph[x]:
		if child in pos:
			pygame.draw.line(pywindow, (255,0,0), pos[x], pos[child], 2)

pygame.display.update()

while True:
	i = 0

