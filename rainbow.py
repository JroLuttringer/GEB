#Draw a rainbow!

for x in range(0,3):
	for y in range(0,255):
		color = [0,0,0]
		color[x] = 255-y
		color[(x+1)%3]=y
		print(color)
		pos_x += 3
