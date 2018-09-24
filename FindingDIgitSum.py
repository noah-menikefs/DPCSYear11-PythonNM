def findSum(n):	
	s = 0;
	x = 0;

	while (n > 0):
		
		x = n%10
		n = n//10
		s = s + x

	return (s);

findSum(720);

def checkHarshad(n):


	if (n%findSum(n)==0):
		return True

	return False

def HarshadStreak(low,high):

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