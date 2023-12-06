digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
operations = ('+', '-', '*', '/', '^')

def isNumber(unit):
    return all(char in digits for char in unit)

def getOper(operation):
    if operation in ('+', '-'):
        return 0
    elif operation in ('*', '/'):
        return 1
    elif operation == '^':
        return 2

def infix_to_postfix(infix):
    stack = []
    output = []

    for token in infix.split(' '):
        if isNumber(token):
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif token in operations:
            opPriority = getOper(token)
            while stack and stack[-1] in operations and getOper(stack[-1]) >= opPriority:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

def getRpn(input):
    infix_expression = input
    postfix_expression = infix_to_postfix(infix_expression)
    return postfix_expression

def calcRpn(rpn):
    stack = []

    for token in rpn:
        if isNumber(token):
            stack.append(token)
        else:
            num2 = float(stack.pop())
            num1 = float(stack.pop())
            result = 0

            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            elif token == '/':
                result = num1 / num2
            elif token == '^':
                result = num1 ** num2

            stack.append(result)

    return stack
def main():
    input_expression = '48 / 4 + 156 * 24 * ( 40 / 5 ) ^ 4'
    rpn_expression = getRpn(input_expression)
    result = calcRpn(rpn_expression)
    
    print(f'Infix expression: {input_expression}')
    print(f'Reverse Polish Notation (RPN): {rpn_expression}')
    print(f"Result: {result[0]}")
if __name__ == '__main__':
    main()