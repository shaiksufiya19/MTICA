class Rectangle:
    
    def __init__(self,length,width):
        assert(length>=0 and width>=0),'Invalid'
        self.length=length
        self.width=width
        
    def calculateArea(self):
        temp=self.width*self.length
        return temp
    def calculatePerimeter(self):
        temp=2*(self.length+self.width)
        return temp
l=int(input('length:'))
w=int(input('width:'))
try:
    ob=Rectangle(l,w)
    area=ob.calculateArea()
    peri=ob.calculatePerimeter()
    print('Area of rectangle is',area)
    print('Perimeter of rectangle is',peri)
except AssertionError as obj:
    print(obj)

#OUTPUT
'''
length:4
width:6
Area of rectangle is 24
Perimeter of rectangle is 20

2nd case:

length:4
width:-8
Invalid
'''
