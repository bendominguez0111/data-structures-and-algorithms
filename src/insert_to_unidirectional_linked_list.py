## Given a unidirectional linked list
## A -> B -> C -> D -> E
## Insert F in between A and B
## A -> B -> C -> F -> D -> E
from __future__ import annotations

class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return "Node {}->{}".format(self.value, self.next_node.value if self.next_node else None)

class LinkedList:
    def __init__(self, head):
        self.head = head

    def show_list(self):
        node = self.head
        str_ = f"{node.value}->"
        while node is not None:
            if hasattr(node.next_node, 'value'):
                str_+=f"{node.next_node.value}->"
            else:
                str_=str_[:-2]
            node = node.next_node

        return str_

    def insert_new_node(self, insert_val, in_front):
        insert_node = self.head
        while insert_node.value != in_front:
            insert_node = insert_node.next_node

        new_next = insert_node.next_node
        new_node = Node(value=insert_val, next_node=new_next)
        insert_node.next_node = new_node
        return

if __name__ == '__main__':
    e = Node(value='E', next_node=None)
    d = Node(value='D', next_node=e)
    c = Node(value='C', next_node=d)
    b = Node(value='B', next_node=c)
    a = Node(value='A', next_node=b)

    linked_list = LinkedList(head=a)
    linked_list.insert_new_node(insert_val='F', in_front='C')
    print(linked_list.show_list())