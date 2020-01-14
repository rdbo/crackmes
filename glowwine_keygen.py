#Crackme Info
#Name: keyGme
#URL: https://crackmes.one/crackme/5c268e8333c5d41e58e00654
#Author: rion
#Language: C/C++
#Level: 1
#------------------
#Length: 5
#Second Char Hex: 64 = '@'
#argv[1][4] + argv[1][3] + argv[1][2] = 300

import random
import string
chars = string.ascii_letters + string.digits

def keygen():
	key = ""
	key += random.choice(chars)
	key += chr(64)
	csum = 0
	while(csum != 300):
		c1 = random.choice(chars)
		c2 = random.choice(chars)
		c3 = random.choice(chars)
		csum = ord(c1) + ord(c2) + ord(c3)
		if(csum == 300):
			key += c1 + c2 + c3
	print(key)

keygen()
