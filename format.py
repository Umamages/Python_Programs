#str format
name='Raja'
age=22
print("hello {} your age is {}".format(name,age))
print("hello {0} your age is {1}".format(name,age))
print("hello {1} your age is {0}".format(name,age))
print("hello %s your age is %s"%(name,age))
print("hello {a}, your age is {b}".format(a=name,b=age))
print("hello {a}, your age is {b}".format(b=name,a=age))
#space holder --> place holder
