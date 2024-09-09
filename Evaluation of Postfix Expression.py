# Example postfix expression
postfix_expression = "23*54*+9-"

stack = []

for char in postfix_expression:
    if char.isdigit(): # Check if the character is a number
        stack.append(int(char))
    else: # Operator encountered
        operand2 = stack.pop()
        operand1 = stack.pop()
        
        if char == '+':
            result = operand1 + operand2
        elif char == '-':
            result = operand1 - operand2
        elif char == '*':
            result = operand1 * operand2
        elif char == '/':
            result = operand1 / operand2
        elif char == '^':
            result = operand1 ** operand2
        
        stack.append(result)

# The final result will be the only element left in the stack
print("The result of the postfix expression is:",stack[0])