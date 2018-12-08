provinces = []
provinces[0] = "britishcolombia"
provinces[1] = "alberta"
provinces[2] = "saskatchewan"
provinces[3] = "manitoba"
provinces[4] = "ontario"
provinces[5] = "quebec"
provinces[6] = "novascotia"
provinces[7] = "newfoundland"
provinces[8] = "newbrunswick"
provinces[9] = "princeedwardisland"

text = text.lower()
text = text.replace(" ", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.replace(".", "")
text = text.replace("?", "")

def hidden(text):
	
	def BC(text):
		for i in range(0, len(text) - 14, 1):
			if (text[i:i+15] == provinces[0]):
				print("British Colombia")

	def 














# f = open("DwiteHiddenGeography.txt", "r")
# for line in f:
# 	text = f.readline()
# 	h = f.readline()
# 	hidden(l,h)

# f.close()