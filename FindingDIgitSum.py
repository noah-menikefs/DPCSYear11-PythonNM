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

	low = 0
	high = 0
	streak = 0
	longStreak = 0

	for i in

for i in range(low,high + 1,1):
	if (checkHarshad(i)):
		score = score + 1;
	else:
		highScore = max(score,highScore)
		score = 0;

highScore = max(score,highScore)
print(highScore)