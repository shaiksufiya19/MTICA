def printSun():
    print('Sunday\n')
    return
def printMon():
    print('Monday\n')
def printTue():
    print('Tuesday\n')
def printWed():
    print('Wednesday\n')
def printThu():
    print('Thursday\n')
def printFri():
    print('Friday\n')
def printSat():
    print('saturday\n')
def choice():
    print("Enter day number between 1-7")
    return
dayDict={1:printSun, 2:printMon, 3:printTue, 4:printWed,
        5:printThu, 6:printFri, 7:printSat}
choice()
dayNo=int(input())
if dayNo>=1 and dayNo<=7:
    dayDict[dayNo]()
else:
    print("Invalid")
