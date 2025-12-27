# Python program
 #reverses an input string using a stack and displays the result:
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, char):
        self.stack.append(char)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return ''

    def is_empty(self):
        return len(self.stack) == 0
    
def reverse_string(input_str):
    s = Stack()

    for char in input_str:          # Push each character onto the stack
        s.push(char)

    reversed_str = ''               # Pop characters to reverse the string
    while not s.is_empty():
        reversed_str += s.pop()

    return reversed_str

# Main Program ---
string = input("Enter a string: ")
reversed_result = reverse_string(string)
print("Reversed String:", reversed_result)