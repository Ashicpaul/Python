expression = "a+b*(c^d-e)^(f+g*h)-i"
stack = []
postfix = []

for char in expression:
    if char.isalnum():  # Check if the character is an operand
        postfix.append(char)
    elif char == '(':  # Push '(' to stack
        stack.append(char)
    elif char == ')':  # Pop from stack until '(' is found
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()  # Remove '(' from stack
    else:  # Operator encountered
        # Define precedence
        if char in ('+', '-'):
            prec = 1
        elif char in ('*', '/'):
            prec = 2
        elif char == '^':
            prec = 3
        else:
            prec = 0
        
        while stack and (
            (stack[-1] in "+-*/^") and
            ((char != '^' and prec <= (1 if stack[-1] in "+-" else 2 if stack[-1] in "*/" else 3)) or
            (char == '^' and prec < 3))
        ):
            postfix.append(stack.pop())
        stack.append(char)

while stack:  # Pop all the remaining operators in the stack
    postfix.append(stack.pop())

print(''.join(postfix))