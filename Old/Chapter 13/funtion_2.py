#user defind function called add

def add(a,b):
    sum=a+b
    print("Sum is ",sum)
#calling function
a = int(input("Enter the first number to add  : "))
b = int(input("Enter the second number to add  : "))
add(a,b)


def subract(a,b):
    ans=a-b
    print("The answer Is ",ans)

#calling function

a = int(input("Enter the first number to subtract  : "))
b = int(input("Enter the second number to subtract  : "))
subract(a,b)

def multiply(a,b):
    product=a*b
    print("The Product Is ",product)

#calling function

a = int(input("Enter the first number to multiply  : "))
b = int(input("Enter the second number to multiply  : "))
multiply(a,b)

def division(a,b):
    Quotient=a/b
    print("Quotient is ",Quotient)


a = int(input("Enter the first number to divide  : "))
b = int(input("Enter the second number to divide  : "))
division(a,b)
