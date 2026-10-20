class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
    def apppend(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=newnode

    def insertat(self,data,pos):
        newnode=Node(data)
        if pos < 1:
            print("invalid position")
        if pos == 1:
            newnode.next=self.head
            self.head=newnode
        else:
            count=1
            prev=None
            temp=self.head
            while temp != None and count < pos:
                prev=temp
                temp=temp.next
                count+=1
            prev.next=newnode
            newnode.next=temp



    def traversal(self):
        if self.head == None:
            print("empty list")
        else:
            temp=self.head
            while temp != None:
                print(temp.data,end=" ")
                temp=temp.next
            print()

sll=SLL()
sll.apppend(10)
sll.apppend(20)
sll.apppend(30)
sll.apppend(40)
sll.traversal()

sll.insertat(25,3)
sll.traversal()