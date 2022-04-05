# NTLM-Hash-checker
A quick and dirty way to check a list of passwords up against a NTLM hash
-----
Example:
python NTLM-hash-checker.py --hash E6B88E914CC592A64422388C19AF8C85 --passwordfile password.txt
order66 is not a match for the hash.
Order66 is not a match for the hash.
oRder66 is not a match for the hash.
ORder66 is not a match for the hash.
orDer66 is not a match for the hash.
OrDer66 is not a match for the hash.
oRDer66 is not a match for the hash.
ORDer66 is not a match for the hash.
ordEr66 is not a match for the hash.
OrdEr66 is not a match for the hash.
oRdEr66 is not a match for the hash.
ORdEr66 is not a match for the hash.
orDEr66 is not a match for the hash.
OrDEr66 is not a match for the hash.
oRDEr66 is not a match for the hash.
ORDEr66 is not a match for the hash.
ordeR66 is not a match for the hash.
OrdeR66 is not a match for the hash.
oRdeR66 is not a match for the hash.
ORdeR66 is not a match for the hash.
orDeR66 is not a match for the hash.
Password found: OrDeR66 -> Match for hash: e6b88e914cc592a64422388c19af8c85
