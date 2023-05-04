# Implement a stack

class Node:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev

    def __repr__(self):
        return "Node {}".format(self.value)

class Stack:

    def __init__(self, head=None, length=0):
        self.head = head
        self.length = length

    def push(self, value):
        node = Node(value=value)

        self.length+=1 

        if not self.head:
            self.head = node
            return
        
        node.prev = self.head
        self.head = node

    def pop(self):

        self.length = max(0, self.length - 1)

        if self.length == 0:
            prev_head = self.head
            self.head = None
            return prev_head

        prev_head = self.head
        self.head = prev_head.prev

        return prev_head.value
    
    def peek(self):
        if self.head:
            return self.head


if __name__ == '__main__':
    s = Stack()
    s.push('A')
    s.push('B')
    s.push('C')
    s.push('D')
    s.pop()
    s.pop()
    print(s.peek()) # Node B