class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CSLL:
    def __init__(self):
        self.head=None
    def apppend(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            newnode.next=self.head #points to it self
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=newnode
            newnode.next=self.head # connects back to head

    
    def traversal(self):
        if self.head == None:
            print("empty list")
        else:
            temp = self.head
            while temp.next != self.head: # traverse till 
                print(temp.data, end=" ")
                temp = temp.next

            print(temp.data)

    def delete(self):
        if self.head == None:
            print("empty list nothing to delete")
        else:
            temp=self.head
            prev=None
            while temp.next != self.head:
                prev=temp
                temp=temp.next
            prev.next=self.head

sll=CSLL()
sll.apppend(10)
sll.apppend(20)
sll.apppend(30)
sll.apppend(40)
sll.traversal()
sll.delete()
sll.traversal()

