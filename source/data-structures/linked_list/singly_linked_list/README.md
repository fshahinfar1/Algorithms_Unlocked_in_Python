# Singly Linked List
This linked list is composed of some nodes (`_Node` class) pointing to each other. LinkeList class has a reference to the first node (`self.head`) and first node has the reference to second and so on.

Computational complexity of inserting to the begining of this linked list is O(1) since `LinkedList` class has a reference to the first node and since `self.end` is reference to the last node appending to this list is about the same order. but for inserting to some arbitary index worst case time complexity is O(n) because LinkedList should traverse to reach the node which will be parent of the new node.

## Implementing notes
* When using indexing syntax with LinkedList the magic function `__getitem__` will be called

## Testing
run `python -m unittest` from this directory to test `singly_linked_list`

## Issues
* `Remove` function is not implemented yet