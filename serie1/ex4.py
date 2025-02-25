# Define functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while (True):
    num1 = float(input("Enter first number: "))
    operator = input("Enter an operator (+, -, *, /) or 'q' to quit :  ")
    while((operator not in operations) and  (operator!="q")):
        operator = input("Enter an operator (+, -, *, /) or 'q' to quit :  ")
        
    #break if user wants to
    if(operator=="q") :
        break;
    num2 = float(input("Enter second number: "))
    
    #do the operation
    if operator in operations:
        result = operations[operator](num1, num2)
        print(f"Result: {result}")
    else:   
        print("Invalid operator")
        
        
        
        
