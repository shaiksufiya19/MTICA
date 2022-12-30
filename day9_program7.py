##def printMonth(dn):
##    pass
##
##
##for i in range(3):
##    inpNum=int(input())
##    print(printMonth(inpNum))


def printMonth(dn):
    if (dn==1):
        return "January"
    elif (dn==3):
        return "March"
    elif (dn==4):
        return "April"
    elif (dn==9):
        return "September"
    elif (dn==12):
        return "December"
    elif (dn==11):
        return "November"
    elif (dn==8):
        return "August"
    else:
        return "Invalid"
for i in range(3):
    inpNum=int(input())
    print(printMonth(inpNum))
    

    

    

    

    

    
