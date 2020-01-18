#Crackme Info
#Name: keygenme
#URL: https://crackmes.one/crackme/5d24585133c5d410dc4d0cbd
#Author: kawaii-flesh
#Language: C/C++
#Platform: Unix/linux etc.
#Level: 2
#------------------
import string
import locale
cmdline = "./keygenme"

def keygen(name):
	csum = 0
	for c in name:
		csum += ord(c)
	char2 = name[0]
	length = len(cmdline)
	check = (csum ^ ord(char2) * 3) << (length & 0x1f)
	return "".join([chr(ord(c)) for c in str(check)])

name = "rdbo"
print(f"Name: {name}")
print(f"Serial: {keygen(name)}")
