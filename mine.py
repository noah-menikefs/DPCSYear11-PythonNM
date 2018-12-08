counter = [0, 0, 0, 0, 0]
letter = []
mine = []

def amsterdam(mine):

	for r in range (0, len(mine), 1):
		for c in range (0, len(mine[r]), 1):
			if (mine[r][c] != "." and  mine[r][c] != "*"):
				letter.append(mine[r][c])
				countSquare(mine,r,c)

	print (letter[0], "-", counter[0])
	print (letter[1], "-", counter[1])
	print (letter[2], "-", counter[2])
	print (letter[3],  "-",  counter[3])
	print (letter[4],  "-", counter[4])

def countSquare(mine, r, c):
	if (r==0 and c==0):
		if (r == "*" and c+1 == "*"):
			counter[(len(letter)-1)] += 1
		if (r+1 == "*" and c == "*"):
			counter[(len(letter)-1)] += 1
		if (r+1 == "*" and c+1 == "*"):
			counter[(len(letter)-1)] += 1
	if (r==0):
		if (r == "*" and c-1 == "*"):
			counter[(len(letter)-1)] += 1	
		if (r == "*" and c+1 == "*"):
			counter[(len(letter)-1)] += 1
		if (r+1 == "*" and c == "*"):
			counter[(len(letter)-1)] += 1
		if (r+1 == "*" and c+1 == "*"):
			counter[(len(letter)-1)] += 1
		if (r+1 == "*" and c-1 == "*"):
			counter[(len(letter)-1)] += 1
	if (c==0):
		if (c == "*" and r-1 == "*"):
			counter[(len(letter)-1)] += 1
		if (c == "*" and r+1 == "*"):
			counter[(len(letter)-1)] += 1
		if (c+1 == "*" and r == "*"):
			counter[(len(letter)-1)] += 1
		if (c+1 == "*" and r+1 == "*"):
			counter[(len(letter)-1)] += 1
		if (c+1 == "*" and r-1 == "*"):
			counter[(len(letter)-1)] += 1
	else:
		if (r-1 == "*" and c-1 == "*"):
			counter[(len(letter)-1)] += 1
		if (r-1 == "*" and c == "*"):
			counter[(len(letter)-1)] += 1
		if (r-1 == "*" and c+1 == "*"):
			counter[(len(letter)-1)] += 1
		if (r == "*" and c-1 == "*"):
			counter[(len(letter)-1)] += 1
		if (r == "*" and c+1 == "*"):
			counter[(len(letter)-1)] += 1
		if (r+1 == "*" and c-1 == "*"):
			counter[(len(letter)-1)] += 1
		if (r+1 == "*" and c == "*"):
			counter[(len(letter)-1)] += 1
		if (r+1 == "*" and c+1 == "*"):
			counter[(len(letter)-1)] += 1
	return counter


amsterdam([["*",".","a","."],["b",".","c","."],[".","*",".","."],[".","d",".","e"]])