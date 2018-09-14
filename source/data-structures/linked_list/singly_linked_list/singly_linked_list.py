class _Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, iterable=None):
        self.head = None
        self.end = None
        self.len = 0
        # add items in iterable object passed in
        if iterable:
            for item in iterable:
                self.append(item)

    def __len__(self):
        return self.len

    def __getitem__(self, indices):
        # linkelist[y]
        if not isinstance(indices, tuple):
            # check for index to be valid
            if indices < 0 or indices >= self.len:
                raise IndexError("index out of range error\
                    while accessing LinkedList")
            ptr = self.head
            for i in range(indices):
                ptr = ptr.next
            return ptr.value
        else:
            raise Exception("LinkedList does not supporting slicing")

        # now handle the different dimensional cases
    def append(self, value):
        # add item to the end of list
        if not self.end:
            self.head = _Node(value)
            self.end = self.head
        else:
            newNode = _Node(value)
            self.end.next = newNode
            self.end = newNode
        self.len += 1

    def insert(self, value, index):
        """
        value: value to be inserted to the linked list
        index: the index value will be placed after insertion
        """
        # check for index to be valid
        if index < 0 or index > self.len:
            raise IndexError("index out of range error\
             while inserting a value into LinkedList")
        # check if the index is end
        elif index == self.len:
            self.append(value)
        # check if the index is front
        elif index == 0:
            newNode = _Node(value, self.head)
            self.head = newNode
            self.len += 1
        else:
            # traverse the list to find the parent of our new node
            parent_ptr = self.head 
            for i in range(index - 1):
                parent_ptr = parent_ptr.next
            # create a new node and set it to point to the rest of list
            # and sent parent to point the new node
            newNode = _Node(value, parent_ptr.next)
            parent_ptr.next = newNode
            self.len += 1

    def remove(self, index):
        pass

    def __iter__(self):
        iter_ptr = self.head
        while iter_ptr:
            yield iter_ptr.value
            iter_ptr = iter_ptr.next

    def __str__(self):
        listValues = list(self)
        return f"LinkedList {listValues}"
