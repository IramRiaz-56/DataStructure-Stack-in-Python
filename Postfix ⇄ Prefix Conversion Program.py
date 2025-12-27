#Postfix ⇄ Prefix Conversion Program 

#Function to convert Postfix to Prefix
def postfix_to_prefix(postfix):
    stack = []
    for ch in postfix:
        if ch.isalnum():  # If character is operand
            stack.append(ch)
        else:  # If character is operator
            op2 = stack.pop()  # Second operand
            op1 = stack.pop()  # First operand
            stack.append(ch + op1 + op2)  # Form prefix and push back to stack
    return stack[-1]  # Final result in stack

#Function to convert Prefix to Postfix
def prefix_to_postfix(prefix):
    stack = []
    for ch in reversed(prefix):      # Reverse the prefix expression
        if ch.isalnum():  # If character is operand
            stack.append(ch)
        else:  # If character is operator
            op1 = stack.pop()  # First operand
            op2 = stack.pop()  # Second operand
            stack.append(op1 + op2 + ch)       # Form postfix and push back to stack
    return stack[-1]  # Final result in stack

#Main Program
print("Choose conversion:")
print("1. Postfix to Prefix")
print("2. Prefix to Postfix")

choice = input("Enter choice (1 or 2): ")      #Take user choice

if choice == '1':
    postfix = input("Enter postfix expression: ")
    result = postfix_to_prefix(postfix)
    print("Prefix:", result)
elif choice == '2':
    prefix = input("Enter prefix expression: ")
    result = prefix_to_postfix(prefix)
    print("Postfix:", result)
else:
    print("Invalid choice.")

