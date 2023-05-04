# Implement a Queue class with:
# constructor method
# enqueue method
# deque method
# peek method
# there is also collections.queue

class QNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def __repr__(self):
        return f"QNode {self.value}"

class Queue:
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def enqueue(self, value):
        # add an element to the queue

        node = QNode(value=value)
        self.length += 1
        #base case
        if not self.tail:
            self.tail = node
            self.head = node

        self.tail.next_node = node
        self.tail = node

    def dequeue(self):
        # push an element from the queue
        
        if not self.head:
            return
        
        self.length -= 1
        prev_head = self.head # pull this out of memory before reassigning the value
        self.head = self.head.next_node # set a new head to the next element

        # free memory, we dont need to do this since Python is garbage collected but for explicity
        prev_head.next = None

        return prev_head.value # return the prev head since this is what we're popping from the queue

if __name__ == '__main__':   
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    queue.enqueue('D')
    queue.dequeue()
    print(queue.head, queue.tail) # QNode B, QNode D