import random
print("\n")
print("******* I'll be guessing the number in your Mind *******")
print("------------------------------------------------------")
print("Imagine a number from 1 to 100")
print("Don't enter the number let me guess!!!\nHit Enter to Continue")
input()
a = random.randint(0,100)
print("Add {}".format(a))
input()
b = random.randint(0,100)
print("Add {}".format(b))
input()
hitta = random.randint(0,100)
print("Add {}".format(hitta))
input()
c = random.randint(0,100)
print("Add {}".format(c))
input()
d = random.randint(0,100)
print("Add {}".format(d))
input()
print("Substract the number you imagined")
input()
i=a+c
j=b+d
print("Substract {}".format(i))
input()
print("Substract {}".format(j))
input()
import random
n = random.randint(1,hitta)
print("Substract {}".format(n))
input()
telepathy = hitta - n
print("The number in your mind is {}".format(telepathy))
