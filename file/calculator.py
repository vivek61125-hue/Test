num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
operation = input("Enter the operation")
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Enter valid operation")        
