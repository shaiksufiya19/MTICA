def printSunday():
    print('Sunday\n')
    return
def printMonday():
    print('Monday\n')
def printTuesday():
    print('Tuesday\n')
def printWednesday():
    print('Wednesday\n')
def printThursday():
    print('Thursday\n')
def printFriday():
    print('Friday\n')
def printSaturday():
    print('saturday\n')
def choice():
    print("0:Sunday")
    print("1:Monday")
    print("2:Tuesday")
    print("3:Wednesday")
    print("4:Thursday")
    print("5:Friday")
    print("6:Saturday")
    print("7:Quit")
    return
DaySelect={0:printSunday, 1:printMonday, 2:printTuesday, 3:printWednesday,
        4:printThursday, 5:printFriday, 6:printSaturday}
selection=0
while True:
    if selection == 6:break
    choice()
    selection=int(input("select a day option:"))
    if (selection>=0) and (selection<6):
        DaySelect[selection]()
    
