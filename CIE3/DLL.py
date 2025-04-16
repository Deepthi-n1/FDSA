class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
    
    def delete_node(self, key):
        temp = self.head
        
        if temp is not None and temp.data == key:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            temp = None
            return
        
        while temp is not None and temp.data != key:
            temp = temp.next

        if temp is None:
            return
        
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next

    def traverse(self):
        if self.head is None:
            print("Doubly linked list is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)
dll.delete_node(10)

dll.traverse()
