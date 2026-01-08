#print ( 2 2) syntax error

"""def calTime():
    min = 0
    sec = int(min) * 60 
    totalSec = min + sec 
    print(input(int("enter min:")))
    print(input(int("enter sec")))
    print("total sec= "+ totalSec)
"""
Welcome = int(input("what you wanna choose \n1:FOR Calculating time \n2:FOR Calculating Distance \nfor your avg pace press any interger \ntype:1 or 2:"))

def timeCal():
    min =int(input("how many min: "))
    sec =int(input("how many sec: "))
    global totalTime
    totalTime = min*60 + sec 
    print(totalTime)

def DistanceCal():
    km = float(input("how km are there: "))
    global conversion
    conversion = km * 1.61 
    print(f"there are {conversion} miles in given Km")

##def pace():
    ##avgpace = ((totalTime/60)/conversion)
def pace():
    avgpace = ((totalTime/60)/conversion)
    print(f"your avg pace was {avgpace}")

if Welcome ==1:
    timeCal()
elif Welcome ==2:
    DistanceCal()
else:
    timeCal()
    DistanceCal()
    pace()
    


