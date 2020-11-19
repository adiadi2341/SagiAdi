import random
r = random.randint(1,100)
print(r)
min = 1
max = 100
text = input("H (higher) / L (lower) / S (success)? \n")
while text != "S":
    if text == "H":
        min = r
        r = random.randint(r,max)
        print(r)
        text = input("H (higher) / L (lower) / S (success)? \n")
    elif text == "L":
        max = r
        r = random.randint(min,r)
        print(r)
        text = input("H (higher) / L (lower) / S (success)? \n")
print("NOICE")