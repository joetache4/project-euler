'''
Joe Walter

difficulty: 5%
run time:   0:00
answer:     129448

	***

059 XOR Decryption

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
'''

from itertools import cycle, product
from data.p059 import get_data

def str_to_ascii(s):
	return [ord(c) for c in s]

def ascii_to_str(a):
	return "".join(chr(c) for c in a)

def xor(code, key):
	return [c^k for c,k in zip(code, cycle(key))]

def get_key(data):
	common_words = ["the"] # this one word is enough to decrypt the text
	ascii        = [a for a in range(ord('a'), ord('z')+1)]
	best         = (-1, None)
	for a,b,c in product(ascii, repeat=3):
		txt      = ascii_to_str(xor(data, [a,b,c]))
		matches  = 0
		for w in common_words:
			matches += txt.count(w)
		best = max(best, (matches, (a,b,c)))
		if best[0] > 10: # arbitrary
			break
	return best[1]

dat = get_data()
key = get_key(dat)
dec = xor(dat, key)
pwd = ascii_to_str(key)
txt = ascii_to_str(dec)
ans = sum(dec)

print(txt)
print(f"key: {pwd}")
print(f"ans: {ans}")
