amt=1
hour=10
while amt<=1024:
    amt=amt*2
    hour=hour+1
if hour>=12:
    print("It takes",hour-12,"pm")
else:
    print("It takes",hour,"am")    
