class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None

    def isEmpty(self):
        return self.top == None

    def push(self,data):
        newnode=Node(data)
        newnode.next=self.top
        self.top=newnode

    def print(self):
        temp=self.top
        while temp:
            print(temp.data)
            temp=temp.next

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            temp=self.top
            print("popped :",temp.data)
            self.top=self.top.next
            temp=None

s=stack()
s.push(10)
s.push(20)
s.push(13)
s.push(14)
s.print()

s.pop()
s.print()