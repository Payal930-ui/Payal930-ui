import random
import string
pass_len=12
char=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(pass_len):
    password+= random.choice(char)
print("your pass is: ",password)
