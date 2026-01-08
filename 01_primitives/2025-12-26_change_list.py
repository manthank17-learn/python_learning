##Python change list 
thislist =["apple", "banana","cherrry"]

"""
def thislistprint():
            thislist[1:3]= [" ackcurrant","watermelon"]   
            print(thislist)
            print(len(thislist))
        thislistprint()
"""
##python list refercening are inclusive and exclusive in nature
"""
         def ChangeList():
            thislist[0 : 3] = ["watermelom"]
            print(thislist)
            ChangeList()
"""
## if python list is update with less the original objects then the list will be update to rules of the new list 


def changelist():
    thislist.insert(2,"watermelon")
    print(thislist)
changelist()

def listAppend():
    thislist.append("orange")
    print()
listAppend()


def itemInsert():
    thislist.insert(1,"orange")
    print(thislist)
itemInsert()

def thisIsExtendList():
    thislist=["apple","banana","cherry"]
    tropical=["mango","pineapple","papaya"]
    thislist.extend(tropical)
    print(thislist)
thisIsExtendList()


def IcanAddanything():
    thistuple = ("kiwi","orange")
    thislist.extend(thistuple)
    print(thislist)
IcanAddanything()
print("\n")
print("this is how u do forLoop")

# this is something about loops
def ForLoopthisway():
    thislist =     [ " apple" , "banana" , "cherry" ]
    for x in thislist:
        print (x)

ForLoopthisway()

def thisIsForExample():
    thislistofmyX = ["Muskan","Loveleen","Noor","Muskan","Khushi"]
    for i in thislistofmyX:
        print("fuck you "+ (i))

    for i in  range    (  len (thislistofmyX)):
        print (thislistofmyX[i])
thisIsForExample()


def whileWallaLoop():
    fruits = ["apple","banana","cherry"]
    i = 0
    while i < len (fruits):
        print(fruits[i])
        i = i + 1 

whileWallaLoop()
