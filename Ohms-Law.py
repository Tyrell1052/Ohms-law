# Ohms law functions

                                  #INPUT FUNCTIONS
#current
def incur():
    dbli = float(input("enter the current"))
    return dbli

#volts
def involt():
    dblv = float(input("enter the volts"))
    return dblv

#resistnce
def inresist():
    dblr = float(input("enter the resistance"))
    return dblr


                                 #PROCESS FUNCTIONS
#resistance
def calcres(dblc, dblvo):
    dblres = dblvo/dblc
    return dblres

#current
def calccur():
    dblcur =
    return dblcur

#volts
def calcvol():
    dblvol =
    return dblvol


                                # OUTPUT FUNCTIONS
# resistance
def outrest(dblr):
    print("the resistance is", format(dblr,".2f"))

#volts
def outvol(dblv):
    print("the volts are", format(dblv,".2f"))

#current
def outcur(dblc):
    print("the current is", format(dblc,".2f"))

# main()
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
