def extract_consonant(s):
    consonant=''
    for i in s:
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            consonant+=i
    return consonant
str1=input()
a=extract_consonant(str1)
print("Consonants in:'",str1,"' is",a)
