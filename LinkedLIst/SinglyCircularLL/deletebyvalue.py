
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

    
    def deletebyvalue(self, data):
        if self.head is None:
            print("Empty list, nothing to delete")
            return

        # Case 1: Delete the head node
        if self.head.data == data:

            # Only one node exists
            if self.head.next == self.head:
                self.head = None
                return

            # Find the last node
            last = self.head
            while last.next != self.head:
                last = last.next

            # Move head and reconnect last node
            self.head = self.head.next
            last.next = self.head
            return

        # Case 2: Delete a non-head node
        prev = self.head
        temp = self.head.next

        while temp != self.head:
            if temp.data == data:
                prev.next = temp.next
                
            prev = temp
            temp = temp.next

        print("Value not found")

    def traversal(self):
        temp=self.head
        while temp.next != self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data)

sll=CSLL()
sll.apppend(10)
sll.apppend(20)
sll.apppend(30)
sll.apppend(40)
sll.traversal()
sll.deletebyvalue(20)
sll.traversal()
sll.deletebyvalue(22)
sll.traversal()

