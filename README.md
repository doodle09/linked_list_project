Linked List Implementation with Node Deletion (Python Project)

This project demonstrates how a singly linked list works internally by building the entire data structure from scratch in Python. It includes creating nodes, adding new nodes, printing the list, and deleting the nth node with proper error handling. The goal is to understand how linked lists behave at a low level without using Python's built-in data structures.

The implementation supports:
• Adding elements to the end of the list
• Displaying all nodes in order
• Deleting a node at a specific position
• Handling errors such as deleting from an empty list, using invalid indices, or accessing out-of-range positions

The project also includes multiple test cases to show how the deletion function responds to real-user scenarios, including interactive input.

Key Features

Custom Node and Linked List Classes
The Node class stores individual data values, and the Singly_linkedlist class manages operations on the linked list.

Robust Delete Function
The delete_nth_node method checks for:
• Empty list
• Negative or zero index
• Index larger than the list length

Interactive Deletion
At the end of the script, users can enter their own index to delete and see the updated linked list immediately.

Demonstration of Edge Cases
The code includes examples for deleting the first node, deleting an out-of-range node, and deleting from an empty list.

Conclusion

This project acts as a practical demonstration of linked list operations and error handling in Python. By manually implementing insertion, traversal, and deletion, it reinforces core data structure concepts commonly asked in interviews and used in algorithm design.
