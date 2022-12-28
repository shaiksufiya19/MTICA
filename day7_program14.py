#remove empty strings
lst1=["Sedan", "SUV", "", "", "Pickup",'',' ']
##ans=[]
##for i in lst1:
##    if i:
##        ans.append(i)
##print(ans)


ans=[i for i in lst1 if i]
print(ans)
