from unittest import TestCase, main
from queue import Queue


class QueueTest(TestCase):

    def test_queue_init(self):
        q = Queue()
        self.assertEqual(len(q), 0)

    def test_queue_enqueue(self):
        q = Queue()
        for i in range(5):
            q.enqueue(i)
        self.assertEqual(len(q), 5)

    def test_queue_peek_empty(self):
        q = Queue()
        with self.assertRaises(Exception):
            q.peek()

    def test_queue_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())

    def test_dequeue(self):
        q = Queue()
        for i in range(5):
            q.enqueue(i)
        val = q.dequeue()
        self.assertEqual(val, 4)
        for i in range(4):
            q.dequeue()
        self.assertTrue(q.is_empty())
        with self.assertRaises(Exception):
            q.dequeue()
        q.enqueue(6)
        self.assertEqual(len(q), 1)

    def test_peek_value(self):
        q = Queue()
        for i in range(5):
            q.enqueue(i)
        self.assertEqual(q.peek(), 4)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.peek(), 2)

    def test_str(self):
        q = Queue()
        for i in range(5):
            q.enqueue(i)

        tmp = [i for i in range(5)]
        expected =  "queue: " + str(tmp)
        self.assertEqual(str(q), expected)






#
# if __name__ == "__main__":
#     main()
