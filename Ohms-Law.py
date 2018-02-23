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
def calccur(dblv, dblr):
    dblcur = dblv/dblr
    return dblcur

#volts
def calcvol(dblr, dblc):
    dblvol = dblr * dblc
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
        # calculate voltage
        dblx = inresist()
        dbly = incur()
        dblx = calcvol(dblx, dbly)
        outvol(dblx)
    elif(strask == "2"):
        print("current")
        # calculate current
        dblx = involt()
        dbly = inresist()
        dblx = calccur(dblx, dbly)
        outcur(dblx)

    elif(strask == "3"):
        print("resistance")
        #calculate resistance
        dblx = incur()
        dbly = involt()
        dblx = calcres(dblx, dbly)
        outrest(dblx)

    elif(strask == "4"):
        strloop = "x"
    else:
        print("bad input")
