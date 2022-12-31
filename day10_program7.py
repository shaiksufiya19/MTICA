fo=open(r"D:\Pythonpractice57\Day10\day10a.txt","a")
for i in range(5):
    inpstr=input("Enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("Written to file")
