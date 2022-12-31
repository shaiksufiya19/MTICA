def printDetail(name,marks=80,age=21):#default argument
    print("Name:",name)
    print("Marks:",marks)
    print("Age:",age)
    return None
#printDetail()      #Type Error
#printDetail('Sufiya')         #missing 'marks' TypeError.
#printDetail('Sufiya',94)
#printDetail(94,'Sufiya')
printDetail(marks=94,name='Sufiya')#keyword argument
