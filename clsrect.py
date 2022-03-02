#Class definition

class rectangle():
    def __init__(self,length,breadth):
          self.length=length
          self.breadth=breadth
      
    def area(self):
        return(self.breadth*self.length)
    
    def perimeter(self):
        return(2*(self.length+self.breadth))

#Main program
l=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(l,b)
print("The area of rectangle=",obj.area())
print("The perimeter of rectangle=",obj.perimeter())
