# Write a program to find remainder when a number is divided by z.

number=int(input("ENTER A NUMBER:"))
z=int(input("ENTER THE DIVISOR:"))
remainder=number%z    # % gives the remainder
print("THE REMAINDER WHEN", number, "IS DIVIDED BY", z, "IS:", remainder)
