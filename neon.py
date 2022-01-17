n=int(input("Enter the number:"))
def neon(s):
    sum=0
    sqr=s*s
    while(sqr>0):
        sum=sum+sqr%10
        sqr=sqr//10
    if(s==sum):
        print("Neon")
    else:
        print("Not Neon")
neon(n)
        
        
    
