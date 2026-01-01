class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoubleLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, new):
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.previous = new
            self.head = new

    def add_tail(self, new):
        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.previous = self.tail
            self.tail = new

    def add_after_to(self, search, new):
        temp = self.head
        while temp.data != search:
            temp = temp.next
        if search != temp.data:
            print("There is no values as " + search + " in this linked list")
            pass
        else:
            new.next = temp.next
            temp.next = new
            new.previous = temp
            temp.next.next.previous = new

    def traverse_forward(self):
        temp = self.head
        while temp is not None:
            print(temp.data + ' --> ', end='')
            temp = temp.next

    def traverse_backward(self):
        temp = self.tail
        while temp is not None:
            print(temp.data + ' --> ', end='')
            temp = temp.previous


c1 = Node('3')
c2 = Node('5')
c3 = Node('6')
c4 = Node('9')
c5 = Node('7')

dll = DoubleLL()
dll.add_front(c1)
dll.add_tail(c2)
dll.add_tail(c3)
dll.add_tail(c4)

print("Before adding 7 the list is like this:")
dll.traverse_forward()
dll.add_after_to('6', c5)
print()

print("After adding 7 the list is like this:")
dll.traverse_forward()
print()

print("The list traversed backward:")
dll.traverse_backward()