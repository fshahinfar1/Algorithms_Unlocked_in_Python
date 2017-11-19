'''
Farbod Shahinfar
95521216
Data Structure Course
Fall 96-97
HW1
Stack
'''

class stack(object):
    def __init__(self):
        '''
        create an empty stack
        '''
        self.__container = []  # type: list
        self.__top = -1  # index of the top element in the list

    def top(self):
        if self.__top == -1:
            raise Exception('Top operation on an empty list')
        return self.__container[self.__top]

    def pop(self):
        if self.__top > -1:
            del self.__container[self.__top]
            self.__top -= 1
        else:
            raise Exception('Can not pop an empty stack')

    def push(self, value):
        self.__container[self.__top+1:] = [value]
        self.__top += 1

    def size(self):
        return self.__top + 1

    def is_empty(self):
        if self.__top == -1:
            return True
        return False

    def __len__(self):
        return self.size()

    def __repr__(self):
        representation = []
        for i in self.__container:
            representation.append(str(i))
        return "stack: "+", ".join(representation)

    def __str__(self):
        return self.__repr__()
