name=input("enter some text:")
a= 0
count = 0                      
while a<len(name):                         #len(name)=uma=3
	if name[a] in ['a','e','i','o','u']:
		print(name[a])		
		count+=1
	a=a+1
else:
	print(count) 