#Crackme Info
#Name: OldSoft's KeyGenMe #2 -- Upgraded from DOS
#URL: https://crackmes.one/crackme/5c9e187b33c5d4419da55648
#Author: wolverine2k
#Language: C/C++
#Platform: Windows
#Level: 1
#------------------
def keygen(name):
	length = len(name)
	counter = 1
	charsum = 0
	r9 = 0
	while(counter <= length):
		sub = counter - 1
		r9 = (charsum + counter + 3)
		counter += 1
		char = name[sub]
		charsum = r9 + ord(char)
	shift = length >> 1
	shift2 = (shift + (shift << 1))
	ssum = shift2 + length
	return ("%d-%d" %(ssum, charsum))

name = "rdbo"
print("Name: " + name)
print("License: " + keygen(name))