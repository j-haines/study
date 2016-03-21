

class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        self.in_stack.insert(0, value)

    def dequeue(self):
        if self.out_stack:
            return self.out_stack.pop(0)
        while self.in_stack:
            self.out_stack.insert(0, self.in_stack.pop(0))
        return self.out_stack.pop(0)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(25)

    assert q.dequeue() == 10

    q.enqueue(30)

    assert q.dequeue() == 25
    assert q.dequeue() == 30
