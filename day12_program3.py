'''set1={10,20,30}
set2={20,40,50}
set1.difference_update(set2)
print(set1)'''


#remove 10,20,30

set1={10,20,30,40,50}
set1.difference_update({10,20,30})
print(set1)


##set1={10,20,30,40,50}
##set2={30,40,50,60,70}
##print(set1.symmetric_difference(set2))#set2=set1 union set1-set2

set1={10,20,30,40,50}
set2={30,40,50,60,70}
set1.symmetric_difference_update(set2)
print(set1)
