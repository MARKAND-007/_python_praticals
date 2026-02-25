# Creating lambda functions
add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else "Error: Division by zero"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = add(num1, num2)

elif operator == '-':
    result = sub(num1, num2)

elif operator == '*':
    result = mul(num1, num2)

elif operator == '/':
    result = div(num1, num2)

else:
    result = "Invalid operator!"

print("Result:", result)
