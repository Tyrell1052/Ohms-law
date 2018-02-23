# Ohms law functions
#input functions
def incur():
    dbli = float(input("enter the current"))
    return dbli
def involt():
    dblv = float(input("enter the volts"))
    return dblv
#inreistance function
#process function

# process functions
def calcres(dblc, dblvo):
    dblres = dblvo/dblc
    return dblres
#calccurrent function
#calcvoltage function
#output function
# output functions
def outrest(dblr):
    print("the resistance is", format(dblr,".2f"))
#outvolts function
#outcurrent function
# main
strloop = "Y"
while(strloop == "Y"):
    print("1. find volts 2. find current 3. find resistance 4. quit")
    strask = input("enter your choice")
    dblx = 0
    dbly = 0
    if(strask == "1"):
        print("volts")
    elif(strask == "2"):
        print("current")
    elif(strask == "3"):
        print("resistance")
        dblx = incur()
        dbly = involt()
        dblx = calcres(dblx, dbly)
        outrest(dblx)
    elif(strask == "4"):
        strloop = "x"
    else:
        print("bad input")
