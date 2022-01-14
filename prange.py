x=int(input("Enter 1st limit:"))
y=int(input("Enter 2nd limit:"))
while(x<=y):
    c=0
    for i in range(1,x+1):
        if(x%i==0):
            c=c+1
    if c==2:
       print(x)
    x=x+1
        
              
                  
              
                  
                
