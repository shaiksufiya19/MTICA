def extract_specialcharacter(s):
    character=''
    for i in s:
        if i in 'BCDFGHvwxyz*%^%&^*(@!#$':
            character+=i
    return character
str1=input()
a=extract_specialcharacter(str1)
print("characters in:'",str1,"' is",a)

