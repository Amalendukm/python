l1=[0,9,3,50]
l2=[78,5,2,10]
print(l1)
print(l2)
c=0
if(len(l1)==len(12)):
    print("Number of elements in both lists are equal")
else:
    print("Number of elements in both lists are  not equal")
    
print("sum of elements in list1:",sum(l1))
print("sum of elements in list2:",sum(l2))
if sum(l1)==sum(l2):
    print("sum of the elements in both lists are equal")
else:
    print("sum of both lists are not equal")
for i in l1:
    if j in l2:
        c=c+1
        print(i)
if c==0:
    print("common element does not exist")
else:
    print("common elements exist")
    
