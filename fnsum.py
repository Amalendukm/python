n=int(input("Enter the number:"))
def sum(x):
    s=l=0
    while(x>0):
        l=x%10
        s=s+l
        x=x//10
    print("sum=",s)
sum(n)
