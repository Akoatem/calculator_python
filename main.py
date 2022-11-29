#store the user input of 2 numbers and the operator
num1, operator, num2 = input("Enter the numbers ").split()
#convert the string into interger
num1 = int(num1)
num2 = int(num2)
# result of operators
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
modulus = num1 % num2

# if + the we need to perform operarion base of addition
# print the result
if operator == "+":
    print("{} + {} = {}".format(num1, num2, sum))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, difference))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, product))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, quotient))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2, modulus))
else:
    print("invalid operators")