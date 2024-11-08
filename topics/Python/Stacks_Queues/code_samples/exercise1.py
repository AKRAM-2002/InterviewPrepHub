#!/usr/bin/python3
'''
Stack implementation using a list
'''
class Stack:
    def __init__(self):
        '''Initialize an empty stack'''
        self.stack = []
    
    def push(self, val):
        '''Add an element to the top of the stack'''
        self.stack.append(val)
    
    def pop(self):
        '''Remove and return the top element of the stack. Return None if empty'''
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def peek(self):
        '''Return the top element of the stack without removing it. Return None if empty'''
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        '''Check if the stack is empty'''
        return len(self.stack) == 0

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.peek())    # Output: 30
    print(stack.pop())     # Output: 30
    print(stack.pop())     # Output: 20
    print(stack.pop())     # Output: 10
    print(stack.pop())     # Output: None (empty stack)
    print(stack.peek())    # Output: None (empty stack)
    stack.push(40)
    print(stack.peek())    # Output: 40
