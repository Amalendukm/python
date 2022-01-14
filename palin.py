n=int(input("Enter number:"))
rev=0
temp=n
while(temp>0):
    d=temp%10
    rev=(rev*10)+d
    temp=temp//10
if(rev==n):
    print("The num is palindrome")
else:
    print("The num is not palindrome")
    
