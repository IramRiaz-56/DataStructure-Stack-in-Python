#Python stack program
#that converts a decimal number to binary
#displays the result:

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        # Display stack from top to bottom
        print("Binary (top → bottom):", ''.join(str(bit) for bit in reversed(self.stack)))


def decimal_to_binary(number):
    s = Stack()
    if number == 0:
        s.push(0)
    else:
        while number > 0:
            remainder = number % 2
            s.push(remainder)
            number //= 2
    s.display()

#--- Main Program ---
try:
    num = int(input("Enter a decimal number: "))
    print(f"Decimal: {num}")
    print("Converted to Binary:")
    decimal_to_binary(num)
except ValueError:
    print("Please enter a valid integer.")