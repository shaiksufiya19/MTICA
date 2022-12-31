def printDetail(name,marks):
    print("Name:",name)
    print("Marks:",marks)
    return None
#printDetail()#Type Error
#printDetail('Sufiya')#missing marks TypeError.
#printDetail('Sufiya',94)
#printDetail(94,'Sufiya')
printDetail(marks=94,name='Sufiya')#keyword argument
