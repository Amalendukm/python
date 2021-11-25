a=int(input("Enter the sub1 mark"))
b=int(input("Enter the sub2 mark"))
c=int(input("Enter the sub3 mark"))
d=int(input("Enter the sub4 mark"))
e=int(input("Enter the sub5 mark"))
total=a+b+c+d+e
print("Total",total)
avg=total/5
print("Average",avg)
if avg>=80:
    print("GOOD")
elif avg>=50:
    print("AVERAGE")
elif avg>=40:
    print("passed")
else:
    print("failed")
