"""
print("hello,world!")           #output:hello,world!

cost = 27.00
rate = .075
print(cost * rate)                 #output:2.025

print(16 + 25 + 92 * 3)            #output:317

word = "python"
for i in word:
    print(i)     

'''output:
p
y
t
h
o
n'''
"""


#  Namespaces and Variable Scoping
"""
print(dir())
print( dir(__builtins__))

text="hello my name is disha gupta".split()
print(text)

# output:['hello', 'my', 'name', 'is', 'disha', 'gupta']
"""


# Exception Handling
"""
!/usr/local/bin/python
x = 7
y = 0
print(x/y)
print("Now we’re done!")

'''output:Traceback (most recent call last):
  File "/workspaces/PYTHON-PROJECTS/BASIC_TO_ADVANCE/1_introduction.py", line 24, in <module>
    print(x/y)
          ~^~
ZeroDivisionError: division by zero'''


x = 7
y = 0
try:
    print(x/y)
except ZeroDivisionError:
    print("Oops- I can’t divide by zero, sorry!")
    print("Now we’re done!") 

'''output:Oops- I can’t divide by zero, sorry! 
Now we’re done!'''
"""

