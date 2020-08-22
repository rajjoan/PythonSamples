# Get user input
num1 = input("Enter a number  : ")
num2 = input("Enter another number  : ")
symbol = input("Enter a symbol (* + - /) : ")

# Subtraction
if symbol == "-":
    if num2 >= num1:
        print(int(num2)-int(num1)) 
    else:
        print(int(num1)-int(num2))
       
# Division
if symbol == "/":
    if num2 >= num1:
        print(float(num2) / float(num1))
    else:
        print(float(num1) / float(num2))
        
# Multiplication
if symbol == "*":
    if num2 > num1:
        print(float(num2) * float(num1))
    else:
        print(float(num1) * float(num2))
        
# Addition
if symbol == "+":
    if num2 > num1:
        print(int(num2) + int(num1))
    else:
        print(int(num1) + int(num2))
      
