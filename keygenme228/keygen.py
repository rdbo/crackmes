#Crackme Info
#Name: keygenme228 by profdraculare
#URL: https://crackmes.one/crackme/5c9e187b33c5d4419da55648
#Author: crackmes.de
#Language: C/C++
#Platform: Unix/linux etc.
#Level: 1
#------------------
#Min serial length: 3
#The next character is greater or equal than the current character
import random
import string

valid_chars = string.ascii_letters
serial_len = 10
step = 1

def keygen():
	key = ""
	char = ''
	while(len(key) == 0):
		char = random.choice(valid_chars)
		if(ord(char) + (step * serial_len) <= ord('z')):
			key += char
	for i in range(serial_len):
		key += chr(ord(char) + step * i)
	return key


print(f"Serial: {keygen()}")
