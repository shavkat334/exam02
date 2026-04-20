
def calculate(num1: float, num2: float, operator: str) -> float:
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Nolga bo'lish mumkin emas"
        result = num1 / num2
    else:
        return "Error: Noto'g'ri operator"
    
    return round(result, 2)

# Test case-lar:
print(calculate(15, 3, "/"))
print(calculate(8, 5, "*"))
print(calculate(10, 0, "/"))
print(calculate(7, 4, "^"))
