
# This functions takes an integer and finds the sum of its digits and returns the sum as an integer
# Pre-conditions: n must be an integer and greater than 0
def findSum(n):	
	s = 0;
	x = 0;

	while (n > 0):
		
		x = n%10
		n = n//10
		s = s + x

	return (s);


def checkHarshad(n):


	if (n%findSum(n)==0):
		return True

	return False

def harshadStreak(low,high):

	low = 250
	high = 500
	streak = 0
	longStreak = 0

	for i in range(low,high+1,1):
		if (checkHarshad(i) == True):
			streak += 1;
		else:
			longStreak = max(streak,longStreak) #finds the max of the two numbers
			streak = 0;

	longStreak = max(streak,longStreak)

	print(longStreak)


#Pre-Condition: n must be a valid string representation of an integer
def findSumStr(n):
	x = 0
	sum = 0
	for i in range(0,len(n), 1):
		x = int(n[i])
		sum = sum + x

	return sum




findSum(720);

# f = open("DwiteHarshadNumbersData.txt", "r")
# for line in f:
# 	l = f.readline()
# 	h = f.readline()
# 	findHarshad(l,h)

# f.close()