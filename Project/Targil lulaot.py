""" תרגיל לולאות 4 1.
num1 = int(input("put a number : \n"))
num2 = num1
while num1 != 0:
    if num1 <= num2 and num1 > 0:
        num2 = num1
    num1 = int(input("put another number: \n"))
print(num2)"""
"""2.
num1 = int(input("put a number: \n"))
while num1>=10:
    num1 //=10
print("the left number is: ", num1)"""
"""3.
num = int(input("put a number: \n"))
i=1
place = i
while i != 7:
    num1 = int(input("put a number: \n"))
    i = i+1
    if num1 > num:
        num = num1
        place = i
print(f"the biggest number is {num} and his place is {place}")"""
"""תרגיל 4 התרגיל הכי קשה שהיה לי עד עכשיו 9.11.20
n1 = int(input("put a number: \n"))
n2=n1
n3 =0
i=0
realnum =0
wow = 0
shit = 0
if n1 <10:
    print (n1, n1*2)
while n1 >= 10:
    n1//=10
    i = i+1
n4=n1
while n2 >= 10:
    shit = wow
    n1 =n2
    n2//=10
    n3 = n1-n2*10
    realnum = n3*(10**i)
    wow = shit +realnum
    i = i-1
wow = wow+n4
print(f"the backnum is {wow}, and the double is {wow*2}")"""
"""5.
n1 = int(input("put a positive number : \n"))
n2 = int(input("put another positive number but smaller: \n"))
if  n1<0 or n2<0:
    print("i said positive number. start again.")
elif n2>=n1:
    print("i said that n2 need to be smaller then n1. start again.")
else:
    print(n1//n2 , n1%n2)"""
"""תרגיל לולאות 3
1-5.
factor = int(input("put the factor: \n"))
factor = factor/100
i=0
a=0
b=0
while i<5:
    grade = int(input("put the grade: \n"))
    i = i+1
    newgrade = int(grade+(grade*factor))
    a = newgrade+a
    b= grade+b
    print(f"the new grade is: {newgrade}")
a=a/5
b=b/5
print(f"average of new grades: {a}")
print(f"average of normal grades: {b}")
print(f"difference of grades: {a-b}")"""
"""תרגיל לולאות 2
1.
grade = int(input("put a grade: \n"))
average = grade
max = 0
i=0
while grade>=0 and grade<=100:
    if max < grade:
        max = grade
    i +=1
    grade = int(input("put a new grade plz: \n"))
    if grade>=0 and grade<=100:
        average = grade +average
print(f"the max grade is: {max}, the average of all grades is: {average/i}, the difference is: {max-(average/i)}")"""
#לולאת for!
# for ___ (שם של משתנה) in range (_) (כמה פעמים אני רוצה שזה יפעל):
#for i in range (x)
#אפשר גם
"""2.
password = input("password plz: \n")
passwordcheck = input("password check plz: \n")
i=1
if password == passwordcheck:
    print("Noice!")
else:
    while password != passwordcheck:
        passwordcheck = input("password check plz, again!: \n")
        i+=1
        if password == passwordcheck:
            print("Noice!")
        elif i==5:
            print("too many tries.")
            break"""
"""3.
n1 = input("put a number: \n")
a=0
for i in n1:
    a = int(i) + a
print(a)"""
#פיבונאצ'י
"""n1 = int(input("put a number: \n"))
x=1
a=0
a1=0
if n1 >= 0:
    print("0")
for i in range(1,n1):
    x = x+a1
    print(x)
    a1=a
    a=x"""