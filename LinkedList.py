# Linked List Data Structure
# 7/13/2023

# node class
class Node:
    # Constructor
    def __init__(self,value):
        self.value = value
        self.next = None

# LinkedList class
class LinkedList:
    # Constructor
    def __init__(self,value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length =+ 1

    # Print LinkedList
    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Append
    def append(self,value):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length =+ 1

    # Pop item at end of LikedList
    def pop_item(self):
        

my_linked_list = LinkedList(4)
my_linked_list.append(6)
my_linked_list.append(8)
my_linked_list.print_linked_list()