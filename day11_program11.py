#Rename key of a dictionary

sample_dict = {
    "name": "Mounika",
    "age": 22,
    "salary": 18000,
    "city": "New york"}
keys=["name","salary"]
sample_dict['location']=sample_dict.pop('city')
print(sample_dict)
