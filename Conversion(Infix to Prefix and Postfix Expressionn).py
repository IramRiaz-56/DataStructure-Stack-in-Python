#stack program 
#Infix to Prefix & Postfix
# precedence of operators
def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0

def infix_to_postfix(exp):             #Convert infix to postfix
    stack = []
    result = ''
    for ch in exp:
        if ch.isalnum():  # operand
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # remove '('
        else:  # operator
            while stack and precedence(ch) <= precedence(stack[-1]):
                result += stack.pop()
            stack.append(ch)
    while stack:
        result += stack.pop()
    return result

def infix_to_prefix(exp):        #Convert infix to prefix
    # Reverse the expression
    exp = exp[::-1]
    # Swap brackets
    exp = ''.join(['(' if ch == ')' else ')' if ch == '(' else ch for ch in exp])
    # Convert to postfix
    postfix = infix_to_postfix(exp)
    # Reverse result to get prefix
    return postfix[::-1]

# Main Program 
infix = input("Enter infix expression: ")

print("\nChoose:")
print("1. Convert to Prefix")
print("2. Convert to Postfix")
choice = input("Enter choice (1 or 2): ")

if choice == '1':
    print("Prefix:", infix_to_prefix(infix))
elif choice == '2':
    print("Postfix:", infix_to_postfix(infix))
else:
    print("Invalid choice.")
