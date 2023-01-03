class Number:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n +1):
            res *=i
        return res
    def checkEvenOdd(self):
        if self.n%2==0:
            return "Even"
        else:
            return "Odd"
    def sumOfDigits(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)
        return t
    def checkArmstrongNumber(self):
        n=str(self)
        l=len(self)
        total=0
        for i in self:
            total +=int(i)**n
        if int(self)==total:
            return 1
        else:
            return 0
    
    
    
inp=int(input())
obj=Number(inp)
print('Factorial of ',inp,'is',obj.calculateFactorial())
print(inp,"is",obj.checkEvenOdd())
print('Sum of Digits Of',inp,'is',obj.sumOfDigits())
print('ArmstrongNumber Of',inp,'is',obj.checkArmstrongNumber())
        
