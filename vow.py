name=input("What is your name?")
print(name)
i=0
count=1
while i<len(name):
    #if name[i]=='a' or name[i]=='e' or name[i]=='o':
    if name[i] in ['a','e','i','o','u']:
        print(name[i])
        count=count+1
    i=i+1
else:
    print(count)      
     