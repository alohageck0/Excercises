import string

strin = input()
upper = string.ascii_lowercase
counter = 0
strin = strin.replace(" ", "").lower()
for letter in upper:
    if letter in strin:
        counter += 1
if counter == len(upper):
    print("pangram")
else:
    print("not pangram")
