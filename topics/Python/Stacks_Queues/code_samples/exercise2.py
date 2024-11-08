from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, val):
        '''Add an element to the end of the queue'''
        self.queue.append(val)
    
    def dequeue(self):
        '''Remove and return the element from the front of the queue. Return None if empty.'''
        if not self.is_empty():
            return self.queue.popleft()
        return None
    
    def peek(self):
        '''Return the front element without removing it. Return None if empty.'''
        if not self.is_empty():
            return self.queue[0]
        return None
    
    def is_empty(self):
        '''Check if the queue is empty'''
        return len(self.queue) == 0

# Example usage
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.peek())    # Output: 10
    print(queue.dequeue()) # Output: 10
    print(queue.dequeue()) # Output: 20
    print(queue.dequeue()) # Output: 30
    print(queue.dequeue()) # Output: None (empty queue)
    print(queue.peek())    # Output: None (empty queue)
    queue.enqueue(40)
    print(queue.peek())    # Output: 40
