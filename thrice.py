x=int(input("Enter 1st num:"))
y=int(input("Enter 2nd num:"))
z=int(input("Enter 3rd num:"))

def thrice(a,b,c):
    s=a+b+c
    if(a==b==c):
        return(3*s)
    else:
        return(s)
print("sum=",thrice(x,y,z))
      
        
