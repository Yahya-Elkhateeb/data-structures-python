class Stack:
    def __init__(self, N):
        self.N = N
        self.arr = [None] * N
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.N - 1

    def push(self, x):
        if not self.is_full():
            self.top += 1
            self.arr[self.top] = x
            print(x, "pushed")
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            val = self.arr[self.top]
            self.top -= 1
            print(val, "popped")
            return val
        else:
            print("Stack is empty")
            return None


s = Stack(5)
for i in range(1, 6):
    s.push(i)

for i in range(5):
    s.pop()
