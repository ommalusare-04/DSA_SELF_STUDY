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
            self.head=newnode
        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            curr.next=newnode
    def traversal(self):
        if self.head==None:
            print("Empty List.")
        else:
            curr=self.head
            while curr != None:
                print(curr.data,end=" ")
                curr=curr.next
            print()

    
    
    def insertat(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        newnode = Node(data)

        if pos == 1:
            newnode.next = self.head
            self.head = newnode
        else:
            count = 1
            prevnode = None
            curr=self.head

            while curr is not None and count < pos:
                prevnode = curr
                curr=curr.next
                count += 1


            newnode.next = prevnode.next
            prevnode.next = newnode




sll=SLL()
sll.append(10)
sll.append(20)
sll.append(30)

sll.traversal()

sll.insertat(40,1)
sll.traversal()
sll.insertat(50,3)
sll.traversal()