a=1
b=2
# a and b are variables 

name="Disha"
print(name)
print(a+b)

# Dataype

a=1  # a is an interger
b=5.22 # b is a floating point number
c="Disha" # c is a string
d=True # d is a boolean variable
e=None # e is a NoneType variable

# Operators


# Arithematic Operators
a=34
b=4
c=a+b  #operators exist in python: +, -, *, /, //, **, %
print(c) #output:38

# Assignment Operators
a=4-2
b=6
b+=3 #incrementing b by 3  
#operators exist in python: +=, -=, *=, /=, //=, **=, %=
print(b) #output:9

# Comparison Operators
d=5<4  #operators exist in python: <, >, <=, >=, ==, !=
print(d) #output:False

# Logical Operators
e=True or False   #operators exist in python: and, or, not
print(e) #output:True


# type()function and type casting
a=5
print(type(a)) #output:<class 'int'>

b=float(a)
print(b) #output:5.0
print(type(b)) #output:<class 'float'>

c="31"
d=int(c)
print(d) #output:31
print(type(d)) #output:<class 'int'>
print(type(c)) #output:<class 'str'>


# input() function

a=input("Enter number1: ")
b=input("Enter number2: ")
print("Number1 is: ", a)     #string input by default
print("Number2 is: ", b)    #string input by default
print("Sum is: ", a+b)   #output:if 2 and 3 then 23 is result
                        #all concatination happens
name1=input("Enter your name: ")
print("Hello ", name1)  #output: Hello Disha

# int()
a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
print("Sum is: ", a+b)   #output: if 2 and 3 then 5 is result

