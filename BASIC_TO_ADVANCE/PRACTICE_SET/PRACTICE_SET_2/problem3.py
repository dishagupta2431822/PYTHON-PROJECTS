# Check the type of variable assigned using input() function.

var=input("ENTER A VALUE:") #default value of the input() function is string.
print("THE VALUE ENTERED IS:", var)
print("THE TYPE OF THE VARIABLE IS:", type(var))

var=int(input("ENTER A VALUE:")) #entered value converted into integer
print("THE VALUE ENTERED IS:", var)
print("THE TYPE OF THE VARIABLE IS:", type(var))

var=float(input("ENTER A VALUE:")) #enetred value converted into float
print("THE VALUE ENTERED IS:", var)
print("THE TYPE OF THE VARIABLE IS:", type(var))

var=bool(input("ENTER A VALUE:")) #any entered value including 0 will be true
print("THE VALUE ENTERED IS:", var)
print("THE TYPE OF THE VARIABLE IS:", type(var))
