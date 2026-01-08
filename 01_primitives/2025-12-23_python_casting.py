a = "Hello, World!"
print (a[0])

for x in "banana" :
    print(x)

b = " this is python casting,sub topic "
print(len(a))

txt = " the best of the thing in life are free"
print("free" in txt)

her_txt="i dont want to meet u"
if "yes" in txt:
    print("yes she is coming.")
else:
    print("fuck off")

c = "hello bitch!"
print(c[2:5])
print(c[:5])
print(c[2:])
print(c[-5:-2])

f = "hello world"
print(f.upper())

##print(f.upper(f.lower()))

g = "  OLA , myniga"
print(g.strip())

h = "hatt dsdk "
print(h.replace("hatt","chall"))

i = "challa, ja, bsdk"
print (i.split("," )) # returns ['Hello', ' World!']

k = a + b
print(k)

def stringFormatting():
    age = 36
    txt = f"My name is John, I am {age}"
    print(txt)

stringFormatting()

def StringFormatting():
    age = 36
    txt = "My name is John, and I am {}"
    print (txt.format (age))
StringFormatting()

def myorder():
    quantity =4
    itemno = 23
    price = 785.5
    myorderValue = "I want {} pieces of item {} for {} dollars."
    print(myorderValue.format(quantity,itemno,price))
myorder()

def whoTheFuckRU():
    txt = "WE are the \"viking\" from the uttar "
    print(txt)
whoTheFuckRU()

def boolcheck():
        x = "hello python"
        y = 15
        z = 0
        print (bool (x))
        print (bool (y))
        print (bool (z))
boolcheck()