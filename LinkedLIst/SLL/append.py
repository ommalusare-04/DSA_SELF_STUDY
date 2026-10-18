class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def append(self,data):
        newnode=Node(data)
        if self.head == None:
            self.head = newnode

        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            curr.next=newnode
    
    def traversal(self):
        if self.head == None:
            print("empty list")
        else:
            curr = self.head
            while curr != None:
                print(curr.data, end=" ")
                curr = curr.next
            print()

sll=SLL()
sll.append(10)
sll.append(20)
sll.append(30)

sll.traversal()

sll.append(40)
sll.traversal()