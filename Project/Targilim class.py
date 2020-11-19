import random
from random import shuffle
"""r = random.randint(1,100)
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
print("NOICE")"""
"""תרגילים מחרוזת 10.11.20 1.
word =input("something: \n")
newword=""
for i in word:
    if i != "a" or i != "A":
        newword = newword + i
print(newword)
פיתרון שני:
name = input("enter name: ")
name = name.replace("A","")
name = name.replace("a","")
print(name)"""

"""2.
username = input("username: \n")
password = ""
for i in range(6):
    password = password + random.choice(username)
print(password)"""

"""3. עדיין לא עובד!!!
w1 = input("enter something: ")
w2 = input("enter other something: ")
k=0
for i in w1:
    if w2.find(i) != -1:
        k1 = w1.count(i)
        k2 = w2.count(i)
        if k1 != 1:
            k = k-1
        k = k + 1
print(k)"""

"""תרגיל 2.3 מהמצגת בעמוד
all = input("write street house nm and town: \n")
all=all.replace(" ", "\n")
print(all)"""
"""street = ""
nm = ""
l = all.split()
for i in l:
    street += i
print(street)"""
#מהקישורים שהיא שמה בכיתת גוגל
#1. שלוש מספרים אמצעיים
"""w = input("put something: ")
length = 0
for i in w:
    length+=1
if length<7 or length%2==0:
    print("not good for u")
else:
    print(w[(length//2)-1:(length//2)+2])"""
#2. לשים סטרינג אחד באמצע סטרינג אחר
"""w = input("put something: ")
middle = input("the thing that will be middle: ")
new=""
for i in range(len(w)):
    if i == len(w)//2:
        new+=middle[0:len(middle)]
    new+=w[i]
print(new)"""
#עוד דרך לעשות את 2.
"""w = input("put something: ")
w2 = input("the thing that will be middle: ")
middle = len(w)//2
left = w[:middle]
right = w[middle:]
print(left+w2+right)"""
#3. אות ראשונה אמצעית ואחרונה משני סטרינגים אחד אחרי השני
"""w = input("put something: ")
w2 = input("the thing that will be middle: ")
middle1 = w[len(w)//2]
middle2 = w2[len(w2)//2]
print(w[0]+w2[0]+middle1+middle2+w[len(w)-1]+w2[len(w2)-1])"""
#4. לסדר סטרינג עם אותיות קטנות קודם
"""w = input("put something: ")
ordered = ""
for i in w:
    if ord(i) >= 97 and ord(i) <= 122:
        ordered += i
for i in w:
    if ord(i) >= 65 and ord(i) <= 90:
        ordered+= i
print(ordered)"""
#5. לספור את כל הכמויות אותיות, ספרות, וסמלים בשורה
"""w = input("put something: ")
chars = 0
digits = 0
symbol = 0
for i in w:
    if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
        chars+=1
    elif ord(i) >= 48 and ord(i) <= 57:
        digits+=1
    else:
        symbol+=1
        if i == " ":
            symbol-=1
print(f"chars = {chars}\n digits = {digits}\n symbols = {symbol}")"""
#7. בדיקה האם סטרינג 1 בתוך סטרינג 2
"""w = input("put something: ")
w2 = input("put another something: ")
a=""
for i in w:
    if i in w2:
        continue
    else:
        a= "False"
        print(a)
if a!="False":
    print("True")"""
#7. למצוא usa במשפט ולספור כמה יש
"""w = input("put something: ")
count = 0
for i in range(len(w)):
    if i != len(w) - 2:
        cake = w[i]+w[i+1]+w[i+2]
        if cake == "usa":
            count+=1
        if cake == "USA":
            count+=1
    else:
        break
print(count)"""
#9. להתעלם מהמילים ולחשב את הממוצע מספרים
"""w = input("put something: ")
num = ""
sum = 0
count = 0
for i in range(len(w)):
    if ord(w[i]) >=48 and ord(w[i]) <=57:
        num+=w[i]
    elif (ord(w[i]) <=48 or ord(w[i]) >=57) and num != "":
        sum+=int(num)
        count+=1
        num=""
if num != "":
    sum+=int(num)
    count+=1
print(f"the sum is:{sum}, and the average is:{sum/count}")"""
#קיימת גם הפונקציה isnumeric שבודקת בtrue אם הסטרינג מורכב רק מספרות
#10. כמות כל אות במשפט
"""w = input("put something: ")
new = ""
for i in range(len(w)):
    if w[i] not in new:
        new += w[i]
        print(f"{w[i]}:",w.count(w[i]))"""
#11. להפוך סטרינג
"""w = input("put something: ")
print(w[::-1])"""
#12. איפה מתחיל הemma האחרון
"""w = input("put something: ")
print(len(w)-w[::-1].find("ammE")-4)""" # זה מינוס 4 כי למילה אמה באנגלית יש 4 אותיות, אז אני רוצה למצוא את ההתחלה של המילה ולא את הסוף
#דרך אחרת ל12 עם rfind
"""w = input("put something: ")
print(w.rfind("Emma"))"""
#13. להפריד לסטרינגים בודדים עם -
"""w = input("put something: ")
while w.find("-") != -1:
    m2 = w[:w.find("-")]
    w=w[w.find("-")+1:]
    print(m2)
print(w)"""
#15. מחיקת סמלים מסטרינג
#הפיתרון הוא עצלני, היה צריך פשוט להוסיף לnew כל עוד אין את התווים המיוחדים מהטבלה של הascii table
"""w = input("put something: ")
new = ""
for i in w:
    if ((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90)) or (ord(i) >= 48 and ord(i) <= 57) or i==" ":
        new+=i
print(new)"""
#16. להוציא הכל חוץ מספרות.
"""w = input("put something: ")
new=""
for i in w:
    if i.isdigit():
        new+=i
print(new)"""
#17. למצוא את המילים שהם גם עם מספר
"""w = input("put something: ")
while w.find(" ") != -1:
    m2 = w[:w.find(" ")]
    w = w[w.find(" ") + 1:]
    for i in m2:
        if i.isdigit():
            print(m2)
            break
for i in w:
    if i.isdigit():
        print(w)
        break"""
#18.