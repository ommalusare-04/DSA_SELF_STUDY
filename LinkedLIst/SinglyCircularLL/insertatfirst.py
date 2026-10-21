class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CSLL:
    def __init__(self):
        self.head=None  
    def append(self,data):
        newnode=Node(data)
        if self.head == None:
            self.head=newnode
            newnode.next=self.head
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head

    def traversal(self):
        if self.head == None:
            print("Empty list")
        else:
            temp=self.head
            while temp.next != self.head:
                print(temp.data,end=" ")
                temp=temp.next
            print(temp.data)

    def insertatfirst(self,data):
        newnode=Node(data)
        if self.head == Node:
            self.head=newnode
            newnode.next=self.head
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            newnode.next=self.head
            temp.next=newnode
            self.head=newnode


sll=CSLL()
sll.append(10)
sll.append(20)
sll.append(30)
sll.traversal()

sll.insertatfirst(5)
sll.traversal()