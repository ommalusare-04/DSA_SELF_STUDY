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
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=newnode

    def traversal(self):
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            while temp != None:
                print(temp.data,end="->")
                temp=temp.next
            print()

    def insertst(self,data,pos):
       
        if pos < 1:
            print("invalid position")
            return
        newnode=Node(data)
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

    def deletebyvalue(self,data):
        if self.head==None:
            print("Empty list nothing to delete")
        else:
            temp=self.head
            if self.head.data == data:
                self.head=self.head.next
            else:
                prev=None
                temp=self.head
                
                while temp != None:
                    if temp.data == data:
                        prev.next=temp.next

                    prev = temp
                    temp = temp.next
                        
    def deleteatlast(self):
        if self.head==None:
            print("Empty list")
        else:
            temp=self.head
            prev=None
            while temp.next != None:
                prev=temp
                temp=temp.next
            prev.next=None
                
            
    def traversalatalt(self):
        if self.head == None:
            print("Empty list")
        else:
            temp=self.head
            while temp != None:
                print(temp.data,end="->")
                temp=temp.next.next
            print()


obj=SLL()
obj.append(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.append(50)
obj.append(60)
obj.traversalatalt()

# obj.insertst(15,2)
# obj.traversal()

# obj.deletebyvalue(20)
# obj.traversal()

# obj.deleteatlast()
# obj.traversal()
