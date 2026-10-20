class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def append(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=newnode
    def traversal(self):
        if self.head==None:
            print("empty list ")
        else:
            temp=self.head
            while temp != None:
                print(temp.data,end="->")
                temp=temp.next
            print()

    def Findmiddle(self):
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            n=0
            while temp != None:
                n+=1
                temp=temp.next

            temp=self.head
            for _ in range(n//2):
                temp=temp.next
            print(temp.data)
        

sll=SLL()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.traversal()

sll.Findmiddle()



