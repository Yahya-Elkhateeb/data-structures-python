class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    def add__front(self, new):
        if self.head == None:
            self.head=new
            self.tail=new
        else:
            new.next=self.head
            self.head=new
    def add__tail(self, new):
        if self.tail == None:
            self.tail=new
            self.head=new 
        else:
            self.tail.next=new
            self.tail=new

    def add__between(self):
        pass
    def traverse(self):
        temp=self.head
        while temp != None:
            print(temp.data)
            temp=temp.next
ll=Linked_List()
c1=Node("Canada")
c2=Node("Netherland")
ll.add__front(c1)
ll.add__tail(c2)
ll.traverse()