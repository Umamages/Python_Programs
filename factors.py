def factors(x):
    for i in range(1, x+1):
        if x % i == 0:
            print(i)
num=int(input("Enter the nubmer:"))
factors(num)            

