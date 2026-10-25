class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None

    def append(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode

    def traversal(self):
        if self.head==None:
            print("empty list")
        else:
            temp=self.head
            while temp.next != None:
                print(temp.data,end=" ")
                temp=temp.next
            print(temp.data)

    
    def deleteatfirst(self):
        if self.head == None:
            print("no node present")
        else:
            temp = self.head
            temp = temp.next

            if temp != None:  # CHANGED: check if another node exists
                temp.prev = None
                self.head=temp

            self.head = temp  # CHANGED: head becomes None if list had one node


dll=DLL()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.traversal()

dll.deleteatfirst()
dll.traversal()

