#Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Mounika",
    "age": 22,
    "salary": 18000,
    "city": "New york"}
keys=["name","salary"]

##newDict={}
##for i in keys:
##    newDict[i]=sample_dict[i]
##print(newDict)
##
##newDict={ i:sample_dict[i] for i in keys }
##print(newDict)


#2nd approach

d={}
for i in keys:
    d[i]=sample_dict[i]
print(d)

d={i:sample_dict[i] for i in keys }
print(d)
