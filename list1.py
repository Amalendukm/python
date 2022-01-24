l1=[0,5,3,50]
l2=[78,5,2,10]
print(l1)
print(l2)
c=0
if(len(l1)==len(l2)):
    print("Lists are equal length")
else:
    print("Sets are  not equal")
if sum(l1)==sum(l2):
    print("sum of the elements in both lists are equal")
else:
    print("sum of both lists are not equal")
for i in l1:
    for j in l2:
        if i==j:
            c=c+1
            print(i)
if c==0:
    print("common element does not exist")
else:
    print("common elements exist")
    
