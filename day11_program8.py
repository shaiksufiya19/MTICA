#Delete a list of keys from a dictionary
sample_dict = {
    "name": "Mounika",
    "age": 22,
    "salary": 18000,
    "city": "New york"}
keys=["name","salary"]
##for k in keys:
##    sample_dict.pop(k)
##print(sample_dict)


d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(d)
