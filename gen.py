def genPossibleValues(list):

	gList = []
	
	for j in range(0,len(list),1):
		for i in range(1,len(list),1):
			temp = list[i]
			list[i] = list[i - 1]
			list[i - 1] = temp
			gList.append(list)

	return gList

print (genPossibleValues([1, 2, 3]))