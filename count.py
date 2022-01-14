s=list(input("Enter a string:"))
i=0
for i in s:
    if(i!=" "):
        c=0
        for j in range(0,len(s)):
            if i==s[j]:
                c=c+1
                s[j]=' '
        print(i,"=",c)
