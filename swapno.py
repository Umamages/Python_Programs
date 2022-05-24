#num1=10
#num2=20

num1=int(input("Enter a Numer: "))
num2=int(input("Enter another Numer: "))
choice=input("Do you want to swap? Yes/No: " )
if choice == 'Yes' or choice == 'yes':
    #Approach 1
    
    #temp=num1
    #num1=num2
    #num2=temp
    
    #Approach 2
    num1,num2=num2,num1
    print(num1)
    print(num2)
else:
    print("Thank you for time")    





