"""
Question: Write a Program to find Factorial of an number using recursive Function
"""

def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

num = int(input("Enter an Number: "))

if num < 0:
   print("Factorial doesn't exist for -ve numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", factorial(num))


"""
OUTPUT:
-----

Enter an Number: 5
The factorial of 5 is 120

"""