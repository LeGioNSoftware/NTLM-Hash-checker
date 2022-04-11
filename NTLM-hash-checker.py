import hashlib
import argparse
import sys

#Set the arguments for hash and passwordfile.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'A bruteforce skript to check a list of passwords up against a NTLM hash by permutating each password')
    parser = argparse.ArgumentParser()
    parser.add_argument('--hash', dest='hash', type=str, help='Enter NTLM hash')
    parser.add_argument('--passwordfile', dest='passwordfile', help='Path to password file')
    args = parser.parse_args()
    
hashsum = args.hash

#The magic behind the permutation.
def permute(inp):
	n = len(inp)
	
	mx = 1 << n

	inp = inp.lower()
	
	for i in range(mx):
		combination = [k for k in inp]
		for j in range(n):
			if (((i >> j) & 1) == 1):
				combination[j] = inp[j].upper()

		temp = ""
		for i in combination:
			temp += i
		if hashsum.lower() == (hashlib.new('MD4', temp.encode('utf-16le')).hexdigest()):
				print("Password found:",temp, "->", "Match for hash:", hashlib.new('MD4', temp.encode('utf-16le')).hexdigest())
				break
		else:
			print(temp, 'is not a match for the hash.')

a_file = open(args.passwordfile)

#Execute the command to permute all the entries in the file containing the passwords.
for password in a_file:    
    permute(password)
