from calculator import Calculator

num1 = int(input("Please enter your first value: "))
operator_val = str(input("Please enter your operator: "))
num2 = int(input("Please enter your second value: "))

calculator = Calculator(num1,num2)

if operator_val == "+":
    print(f"The value of your addition is {calculator.addition()}")
    
elif operator_val == "-":
    print(f"The value of your subtraction is {calculator.subtraction()}")
    
elif operator_val == "*":
    print(f"The value of your addition is {calculator.multiplication()}")
    
elif operator_val == "/":
    print(f"The value of your addition is {calculator.division()}")
    
elif operator_val == "%":
    print(f"The value of your addition is {calculator.mod()}")
else:
    print("Error")
