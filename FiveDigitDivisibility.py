
def genList(D1):


	numList = []

	for i in range(1, D1 + 1, 1):
		numList.append(i)

	return numList


def swapList(numList):

	numSwap = []

	temp = 0

	for i in range(0, len(numList), 1):

		for i in range(0, len(numList) - 1, 1):

			temp = numList[i + 1]

			numList[i + 1] = numList[i]

			numList[i] = temp

			numSwap.append(genNum(numList))

	return numSwap	


def genNum(numList):

	swapStr = ""

	for i in range(0,len(numList),1):

		swapStr = swapStr + str(numList[i])

	return int(swapStr)

def checkDiv(numSwap, D2):

	ctr = 0

	for i in range(0,len(numSwap), 1):

		if (numSwap[i] % D2 == 0):
			ctr = ctr + 1

	return ctr

numList = (genList(9))

numSwap = swapList(numList)


print (checkDiv(numSwap, 24))


