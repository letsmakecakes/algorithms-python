# Singly Linked List Implementation in Python

A comprehensive implementation of a Singly Linked List data structure with various operations and thorough documentation.

## Features

- **Basic Operations**
  - Append (add to end)
  - Prepend (add to start)
  - Pop (remove from end)
  - Pop First (remove from start)
  - Get node at index
  - Set value at index
  - Insert at index
  - Remove at index
  - Reverse list

- **Additional Features**
  - Length property
  - String representation
  - Comprehensive error handling
  - Edge case management

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/singly-linked-list.git
cd singly-linked-list
```

## Usage

```python
# Create a new linked list
my_list = SinglyLinkedList(5)  # Creates a list with initial value 5

# Add elements
my_list.append(10)      # Add to end: 5 -> 10
my_list.prepend(1)      # Add to start: 1 -> 5 -> 10

# Access elements
node = my_list.get(1)   # Get node at index 1 (value: 5)
my_list.set_value(1, 7) # Change value at index 1: 1 -> 7 -> 10

# Remove elements
my_list.pop()           # Remove from end: 1 -> 7
my_list.pop_first()     # Remove from start: 7

# Other operations
my_list.insert(1, 15)   # Insert at index: 7 -> 15
my_list.remove(0)       # Remove at index: 15
my_list.reverse()       # Reverse the list

# Get list information
length = len(my_list)   # Get number of nodes
print(my_list)          # Print list: "15"
```

## API Reference

### Class: ListNode

```python
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Class: SinglyLinkedList

#### Constructor

- `__init__(initial_value)`: Initialize list with a single node

#### Methods

| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `append(value)` | Add node to end | O(1) |
| `prepend(value)` | Add node to start | O(1) |
| `pop()` | Remove & return last node | O(n) |
| `pop_first()` | Remove & return first node | O(1) |
| `get(index)` | Get node at index | O(n) |
| `set_value(index, value)` | Update value at index | O(n) |
| `insert(index, value)` | Insert node at index | O(n) |
| `remove(index)` | Remove node at index | O(n) |
| `reverse()` | Reverse the list | O(n) |
| `__len__()` | Get list length | O(1) |
| `__str__()` | Get string representation | O(n) |

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Access | O(n) |
| Search | O(n) |
| Insertion | O(1) to O(n) |
| Deletion | O(1) to O(n) |

## Space Complexity

- **Storage**: O(n)
- **Additional Space**: O(1) for most operations