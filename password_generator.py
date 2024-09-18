import random
import string
List=[]
password=[]
length=int(input("Enter the length of your password:\n"))
List += string.ascii_letters
List += string.digits
List += string.punctuation
for i in range(length):
    password.append(random.choice(List))
print("Here Your Password:\t\""+''.join(password)+"\"")
