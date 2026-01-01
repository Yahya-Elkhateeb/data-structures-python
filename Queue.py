class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


q = Queue()
q.enqueue('N')
q.enqueue('A')
q.enqueue('H')
q.enqueue('R')
q.enqueue('İ')
q.enqueue('M')
q.enqueue('E')

st = Stack()

while not q.is_empty():
    st.push(q.dequeue())

while not st.is_empty():
    print(st.pop())