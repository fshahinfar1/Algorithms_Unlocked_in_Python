class Node(object):
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None


class BinaryTree(object):
    def __init__(self, data=None):
        self.__root = Node(data)
