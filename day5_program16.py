def extractDigit(s):
    digit=''
    for i in s:
        if i in '1234565':
            digit+=i
    return digit
str1=input()
a=extractDigit(str1)
print("Digits in:'",str1,"' is",a)

