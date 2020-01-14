#Crackme Info
#Name: glow wine [keygen practice]
#URL: https://crackmes.one/crackme/5df26b4033c5d419aa013362
#Author: Bkamp
#Language: C/C++
#Platform: Unix/linux etc.
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
