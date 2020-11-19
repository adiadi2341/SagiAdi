import random
from random import randint
#list [], like: x = [1,2,3,4,5] - list of 5 integers.
"""x = [1,2,3,4,5]
print(x)
x=x+[1]
print(x)
x.append(74)
print(x)
x[4]=14135
print(x)
print(len(x))
x.remove(14135)
print(x)"""
#האתר שאורלי נתנה לנו, https://pynative.com/python-list-exercise-with-solutions/
"""1.
aLsit = [100, 200, 300, 400, 500]
print(aLsit[1::2])"""
"""2.
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list4 = []
for i in range(0,4):
    list3 = [list1[i]+list2[i]]
    list4 = list4 + list3
print(list4)"""
"""3."""
"""aList = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(aList)):
    aList[i] = aList[i]**2
print(aList)"""
#הפיתרון שלהם לסעיף 3
"""aList = [1, 2, 3, 4, 5, 6, 7]
aList =  [x * x for x in aList]
print(aList)"""
"""4.
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
newlist = [x+y for x in list1 for y in list2]
print(newlist)"""
#תרגיל 14. מהאתר https://pynative.com/python-string-exercise/
"""l = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
for i in l:
    if i == "" or i == None:
        l.remove(i)
print(l)"""
#עוד פתרון הוא שימוש בפונקציה filter אשר נמצאת בתוך הList. (
#תרגיל 5.6 מהמצגת
"""l = [1,2,3,4,5,6,7,8,9,10]
l2=[]
print(l[len(l)-3:])
print(l[::-1])
print(l[::2])
for i in l:
    if i%2!=0:
        l2.append(i)
print(l2)
for i in range(3):
    nm = int(input("pick a number: "))
    if i < 2:
        l[4+i] = nm
    else:
        l.append(nm)
print(l)
l = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    l[i]*=2
print(l)
l = [1,2,3,4,5,6,7,8,9,10]
l3 = [l[0],l[len(l)-1]]
print(l3)"""
#פייתון תרגילים רשימות 1.
"""l=[]
for i in range(10):
    l.append(randint(1,101))
print(l)"""
#2. ליצור רשימה שמכילה את כל המספרים מ1-10
"""l=[]
for i in range(10):
    l.append(i+1)
print(l)"""
#3. צור רשימה שמכילה את שלושת המספרים האחרונים של l
#l=[1,2,3,4,5,6,7,8,9,10]       #משמש לכל התרגילים מ3-12
"""l2 = l[len(l)-3:len(l)]
print(l2)"""
#ביטול תרגילים, 3-8 הם אותו דבר כמו 5.6 מהמצגת
#תרגיל 5.1 במצגת
"""j = int(input("how much numbers u want to put in?: "))
l=[]
for i in range(j):
    i=int(input("put a number: "))
    l.append(i)
print(f"max: {max(l)}")
print(f"min: {min(l)}")
print(f"average: {sum(l)/len(l)}")"""