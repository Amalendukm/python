l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
rec=lambda l,b:(l*b)
print("Area of Rectangle",rec(l,b))
s=int(input("Enter the side length:"))
sqr=lambda s:(s*s)
print("Area of square",sqr(s))
b=int(input("Enter the breadth:"))
h=int(input("Enter the height:"))
t=lambda b,h:(0.5*b*h)
print("Area of Triangle",t(b,h))


