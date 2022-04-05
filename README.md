# NTLM-Hash-checker
A quick and dirty way to check a list of passwords up against a NTLM hash.
Where it will permute the letters in the passwords and test all the different versions up against the NTLM hash.

-----

Example:
python NTLM-hash-checker.py --hash E6B88E914CC592A64422388C19AF8C85 --passwordfile password.txt
![image](https://user-images.githubusercontent.com/66059685/161746844-004b3921-30de-41e5-8c1b-c086ca2043f8.png)
