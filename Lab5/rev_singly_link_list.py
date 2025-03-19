class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None  # prev is the new tail
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

# Define the node values
a, b, c, d = "a", "b", "c", "d"

# Create the linked list
node1 = Node(a)
node2 = Node(b)
node3 = Node(c)
node4 = Node(d)

node1.next = node2
node2.next = node3
node3.next = node4

# Print the original linked list
print("Original Linked List:")
print_list(node1)

# Reverse the linked list
reversed_head = reverse_linked_list(node1)

# Print the reversed linked list
print("Reversed Linked List:")
print_list(reversed_head)
