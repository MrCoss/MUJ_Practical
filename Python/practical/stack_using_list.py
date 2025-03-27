# Write a Python program to implement a stack using lists and perform push, pop, and display operations.

class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list as the stack

    def push(self, item):
        self.stack.append(item)  # Add item to the top of the stack
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the top item
        else:
            print("Stack is empty!")

    def display(self):
        if not self.is_empty():
            print("Stack elements:", self.stack[::-1])  # Display elements from top to bottom
        else:
            print("Stack is empty!")

    def is_empty(self):
        return len(self.stack) == 0  # Check if the stack is empty

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
s.display()

