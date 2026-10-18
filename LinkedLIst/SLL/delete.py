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
            print("Empty List")
        else:
            curr=self.head
            while curr != None:
                print(curr.data,end=" ")
                curr=curr.next
            print()

    def insertat(self,data,pos):
        newnode=Node(data)
        if pos < 1:
            print("invalid position")
            return
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

    def delete(self):
        if self.head == None:
            print("nothing to delete")
        else:
            temp=self.head
            self.head=temp.next

    def deleteatlast(self):
        if self.head == None:
            print("nothing to delete")
        else:
            temp=self.head
            prev=None
            while temp.next != None:
                prev=temp
                temp=temp.next
            prev.next=None

    def deleteByvalue(self,valu)


sll=SLL()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traversal()
sll.insertat(15,2)
sll.traversal()
sll.delete()
sll.traversal()
sll.deleteatlast()
sll.traversal()