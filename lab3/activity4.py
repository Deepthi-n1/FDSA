class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def search_node(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# Example
sll = SinglyLinkedList()

# Append node
sll.append_node(10)
sll.append_node(20)
sll.append_node(30)

# Display the list
print("Linked list after appending 10, 20, 30:")
sll.linked_list()

# Search for a node
print("\nSearching for node with data 20:")
print("Node found:" if sll.search_node(20) else "Node not found")

# Display the list
print("\nTraversing the linked list:")
sll.linked_list()
