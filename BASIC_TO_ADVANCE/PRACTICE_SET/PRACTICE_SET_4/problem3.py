# Check that a type cannot be changed in python.

a=(34,234,"Disha",9.5)
print(type(a))  #<class 'tuple'> (a is a tuple)
a[0]=45  #TypeError
print(a)