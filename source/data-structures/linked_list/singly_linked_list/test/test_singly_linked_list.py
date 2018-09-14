from unittest import TestCase, main
from singly_linked_list import LinkedList


class LinkedListTest(TestCase):

    def test_linked_list_init(self):
        linkedList = LinkedList()
        self.assertEqual(len(linkedList), 0)

    def test_linked_list_append(self):
        myList = LinkedList()
        for i in range(10):
            myList.append(i)
        self.assertEqual(len(myList), 10)
        # test iterating over list and check if every
        # thing is expected
        expectedValue = 0
        for value in myList:
            self.assertEqual(value, expectedValue)
            expectedValue += 1

    def test_linked_list_str(self):
        simpleList = [i for i in range(10)]
        myList = LinkedList(simpleList)
        expectedString = f"LinkedList {simpleList}"
        self.assertEqual(str(myList), expectedString)

    def test_linked_list_insert(self):
        myList = LinkedList()  # create a new linked list
        myList.insert(3, 0)
        myList.insert(2, 0)
        myList.insert(1, 0)
        self.assertEqual(myList[2], 3)
        self.assertEqual(len(myList), 3)
        expectedValue = 1
        for value in myList:
            self.assertEqual(value, expectedValue)
            expectedValue += 1

        myList.insert(4, 3)
        self.assertEqual(len(myList), 4)
        self.assertEqual(myList[3], 4)
        myList.insert(1.5, 2)
        self.assertEqual(myList[2], 1.5)