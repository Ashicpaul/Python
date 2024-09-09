arr = 4

stack = []
top = -1

if top < arr - 1:
    top += 1
    stack.append(120)
else:
    print("Error: Overflow")

if top < arr - 1:
    top += 1
    stack.append(110)
else:
    print("Error: Overflow")

if top < arr - 1:
    top += 1
    stack.append(100)  
else:
    print("Error: Overflow")
   

if top < arr - 1:
    top += 1
    stack.append(100)  
else:
    print("Error: Overflow")
   
if top < arr - 1:
    top += 1
    stack.append(100)  
else:
    print("Error: Overflow")
   
if top < arr - 1:
    top += 1
    stack.append(100)  
else:
    print("Error: Overflow")
   
   
print("Stack contents:")

for i in range(top, -1, -1):
    print(stack[i])


if top != -1:
    popped_value = stack[top]
    top -= 1
    print("Popped value:", popped_value)
else:
    print("Stack underflow")



print("Stack contents after pop:")
for i in range(top, -1, -1):
    print(stack[i])
