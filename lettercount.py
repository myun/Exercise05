from sys import argv
script,filename = argv

f = open(filename)
filetext = f.read()
filetext = filetext.lower()
letters = list(filetext)

alphabet = [0] * 26

for letter in letters:
    index = ord(letter) - 97
    if index > 25 or index < 0:
        continue
    else: 
        alphabet[index] += 1

for alpha in alphabet:
    print alpha
#For a spark graph type python lettercount.py twain.txt | spark

f.close()