"""
Implementation of a Singly Linked List data structure with comprehensive operations.
This implementation provides basic and advanced operations on a singly linked list
with proper error handling and edge cases management.
"""

class ListNode:
    """
    A node in a singly linked list.
    
    Attributes:
        value: The data stored in the node
        next: Reference to the next node in the linked list
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    """
    A singly linked list implementation with various operations.
    
    Attributes:
        head: First node of the linked list
        tail: Last node of the linked list
        size: Number of nodes in the linked list
    """
    def __init__(self, initial_value):
        """
        Initialize the linked list with a single node.
        
        Args:
            initial_value: The value to be stored in the first node
        """
        initial_node = ListNode(initial_value)
        self.head = initial_node
        self.tail = initial_node
        self.size = 1

    def append(self, value):
        """
        Add a new node with the given value at the end of the list.
        
        Args:
            value: The value to be appended
            
        Returns:
            bool: True if the operation was successful
        """
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return True

    def prepend(self, value):
        """
        Add a new node with the given value at the start of the list.
        
        Args:
            value: The value to be prepended
            
        Returns:
            bool: True if the operation was successful
        """
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return True

    def pop(self):
        """
        Remove and return the last node in the list.
        
        Returns:
            ListNode: The removed node, or None if list is empty
        """
        if not self.head:
            return None
        
        if self.size == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return popped_node

        current = self.head
        new_tail = current
        while current.next:
            new_tail = current
            current = current.next
        
        self.tail = new_tail
        self.tail.next = None
        self.size -= 1
        return current

    def pop_first(self):
        """
        Remove and return the first node in the list.
        
        Returns:
            ListNode: The removed node, or None if list is empty
        """
        if not self.head:
            return None

        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.size -= 1

        if self.size == 0:
            self.tail = None
        
        return popped_node

    def get(self, index):
        """
        Get the node at the specified index.
        
        Args:
            index: Zero-based index of the node to retrieve
            
        Returns:
            ListNode: The node at the specified index, or None if index is invalid
        """
        if not 0 <= index < self.size:
            return None
        
        current = self.head
        for _ in range(index): 
            current = current.next
        
        return current

    def set_value(self, index, value):
        """
        Update the value of the node at the specified index.
        
        Args:
            index: Zero-based index of the node to update
            value: New value to set
            
        Returns:
            bool: True if the update was successful, False otherwise
        """
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Insert a new node with the given value at the specified index.
        
        Args:
            index: Zero-based index at which to insert
            value: Value to insert
            
        Returns:
            bool: True if the insertion was successful, False otherwise
        """
        if not 0 <= index <= self.size:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.size:
            return self.append(value)
        
        new_node = ListNode(value)
        previous = self.get(index - 1)
        new_node.next = previous.next
        previous.next = new_node
        self.size += 1
        return True

    def remove(self, index):
        """
        Remove and return the node at the specified index.
        
        Args:
            index: Zero-based index of the node to remove
            
        Returns:
            ListNode: The removed node, or None if index is invalid
        """
        if not 0 <= index < self.size:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.size - 1:
            return self.pop()
        
        previous = self.get(index - 1)
        removed_node = previous.next
        previous.next = removed_node.next
        removed_node.next = None
        self.size -= 1
        return removed_node

    def reverse(self):
        """
        Reverse the linked list in-place.
        
        Returns:
            bool: True if the operation was successful
        """
        if self.size <= 1:
            return True
        
        previous = None
        current = self.head
        self.tail = self.head
        
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        self.head = previous
        return True

    def __len__(self):
        """Return the number of nodes in the list."""
        return self.size

    def __str__(self):
        """Return a string representation of the list."""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)