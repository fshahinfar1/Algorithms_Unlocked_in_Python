class Node(object):
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @property
    def left(self):
        return self.__left

    @left.setter
    def set_left(self, value):
        if not isinstance(value, Node):
            raise Exception("Type `Node` expected")
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def set_right(self, value):
        if not isinstance(value, Node):
            raise Exception("Type `Node` expected")
        self.__right = value

class BinarySearchTree(object):
    def __init__(self, data_type, data=None):
        self.__root = Node(data)
        self.__data_type = data_type

    def _find_parent(self, data):
        if not isinstance(data, self.__data_type):
            raise Exception("Inserting value of unknown type")
        node = self.__root
        while (True):
            if data <= node.data:
                if node.left:
                    node = node.left
                else:
                    return node
            else:
                if node.right:
                    node = node.right
                else:
                    return node

    def insert(self, data):
        node = self._find_parent(data)
        if data <= node.data:
            node.left = Node(data)
        else:
            node.right = Node(data)

    def contains(self, data):
        node = self._find_parent(data)
        return data == node.data

    def remove(self, data):
        pass
