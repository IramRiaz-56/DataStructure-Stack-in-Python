# Complete Stack Program
# Stack class using List
class Stack:
    def __init__(self):
      self.stack = []                          # Initialize an Empty List to Represent the Stack
    def push(self , value):                    # Add Value to the Top of the Stack
       self.stack.append(value)
       print(f"{value} pushed to stack")
    def pop(self):                             # Remove the Top Element fron the stack
       if not self.is_empty():                 # Check if Stack is Empty or not
        removed = self.stack.pop()
        print(f"popped: {removed}")
       else:
          print("stack is empty")
    def display(self):                         #Display the Stack from Top to Bottom 
              if not self.is_empty():
               print("stack(top->  bottom):", list(reversed(self.stack)))
              else:
                print("stack is empty!")
    def display_reversed(self):                   #Display the Stack from Bottom to Top
        if not self.is_empty():
            print("stack(bottom->top):", self.stack)
        else:
            print("stack is empty!")
    def size(self):                               #Print the Number of Element in the Stack
        print("size of stack:", len(self.stack))
    def is_empty(self):                           #Check if  the Stack is Empty
        return len(self.stack) == 0
#---Main Program with Menu ---
s = Stack()                                #Create an Object of the Stack Class
while True:                                # Infinite Loop to keep the menu running
    print("\n--- Stack Menu---")
    print("1. push(multiple value)")
    print("2. pop")
    print("3. Display Stack")
    print("4. Display Reversed")
    print("5. Size")
    print("6. Exist")

    choise = input("Enter your choice (1-6):")
    if choise == '1':
       try:
           n = int(input("How Many Values do you want to push?"))
           for i in range(n):
                 val = input(f"enter value {i+1}: ")
                 s.push(val)                  # Push each value in to the Stack 
       except ValueError :
            print("please enter a valid number.")
    elif choise == '2':
        s.pop()                          # Call Method
    elif choise == '3':
        s.display()
    elif choise == '4':
        s.display_reversed()
    elif choise == '5':
        s.size()
    elif choise == '6':            
        print("exiting program.")            
        break                   # Exit the Loop and End the Program
    else:
        print("Invalid choice. Try again.")
