class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_node(self, data):
        if not self.head:
            print("The list is empty!")
            return

        current = self.head
        while current and current.data != data:
            current = current.next

        if current is None:
            print(f"Node with data {data} not found!")
            return

        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

        if current == self.head:
            self.head = current.next

    def traverse_forward(self): 
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

# Example usage
dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("After insertions:")
dll.traverse_forward()

dll.delete_node(20)
print("After deleting node 20:")
dll.traverse_forward()
