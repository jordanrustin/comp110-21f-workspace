"""This uses numeric operators to output mathematical operations of two variables."""
__author__ = "730308364"

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")

a = int(left)
b = int(right)

exponential = a ** b
divide = a / b
integer_divide = a // b
remainder = a % b

print(str(a) + " ** " + str(b) + " is " + str(exponential) ) 
print(str(a) + " / " + str(b) + " is " + str(divide))
print(str(a) + " // " + str(b) + " is " + str(integer_divide) )
print(str(a) + " % " + str(b) + " is " + str(remainder) )