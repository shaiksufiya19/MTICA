sample_dict = {
    "name": "Mounika",
    "age": 22,
    "salary": 18000,
    "city": "New york"}
keys=["name","salary"]
res=dict()
for k in keys:
    res.update({k:sample_dict[k]})
print(res)
