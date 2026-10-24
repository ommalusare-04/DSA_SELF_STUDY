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
        if self.head == None:
            self.head = newnode
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp
            

    def traversal(self):
        if self.head==None:
            print("empty list")
        else:
            temp=self.head
            while temp.next != None:
                print(temp.data,end=" ")
                temp=temp.next
            print(temp.data)

dll1=DLL()
dll1.append(10)
dll1.append(20)
dll1.append(30)
dll1.traversal()