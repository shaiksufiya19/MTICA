Lst=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in Lst:
##    if i*i >50:
##        ans.append(i*i)
##print(ans)
#to find square root is greater than 50. 


ans=[ i*i for i in Lst if i*i >50]
print(ans)
