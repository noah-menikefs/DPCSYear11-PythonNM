cardstring = "49927398716"
card = int(cardstring)
length = len(card)

def findSum(cardstring):	
	s = 0;

	while (card > 0):
		
		x = card%10
		card = card//10
		s = s + x

	return (s)

def cardSum(cardstring):
	ctr = 0
	sum = 0
	for i in range(length-1, -1, -1):
		if (ctr % 2 == 1):
			temp = int(cardstring[i])
			temp = temp * 2
			if (temp >= 10):
				sum = sum + temp % 10
				temp = temp // 10
			sum = sum + temp
		else:
			sum = sum + cardstring[i]

if (sum % 10 == 0):
	print ("VALID")
else:
	print ("INVALID")			
		

# f = open("CreditCardData.txt", "r")
# for line in f:
# cardstring = f.readline()
# 	cardSum(cardstring)

# f.close()
