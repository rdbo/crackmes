#Size == 16
#Characters >= 'A' and <= 'Z'
#Characters >= '0' and <= '9'
#while(true)
#local_c = (local_c + argv[local_10] >> 1) % 3840 + 10
#0xf00
#local_10 += 1 
#return (local_c == (int)argv[length - 1])

import random
import string
valid_chars = string.ascii_uppercase + string.digits

def keygen():
	valid_key = False
	while(valid_key == False):
		key = ""
		csum = 0
		while(len(key) < 15):
			key += random.choice(valid_chars)
		for c in key:
			csum += ord(c)
			csum = csum >> 1
			csum %= 3840
			csum += 10
		final = chr(csum)
		if(final in valid_chars):
			key += final
			valid_key = True
			print(key)

keygen()