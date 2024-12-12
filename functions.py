

def name_returner(name: str) -> str:
    print(name)


def calculator(a: float, b: float, sign: str):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == 'x' or sign == '*':
        return a * b 
    elif sign == '/':
        return a / b
    else: return 'enter the right sign'

output = calculator(4, 4, '/')        
print(output)