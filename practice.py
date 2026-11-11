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
                temp = temp.next
            temp.next=newnode

    def print(self):
        temp=self.head
        if self.head == None:
            print("empty list")
        while temp != None:
            print(temp.data,end=" ")
            temp=temp.next
        print()

    def insertatfirst(self,data):
        newnode=Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next=self.head
            self.head=newnode
    
    def InsertAnyPos(self,data,pos):
        newnode=Node(data)
        if pos == 1:
            newnode.next=self.head
            self.head=newnode

        else:
            prev=None
            temp=self.head
            count=1
            while temp != None and count < pos:
                prev=temp
                temp=temp.next
                count+=1
            prev.next=newnode
            newnode.next=temp

    def deleteAtFirst(self):
        if self.head == None:
            print("empty list")
        else:
            self.head=self.head.next


    def deleteAtLast(self):
        if self.head == None:
            print("empty list")
        elif self.head.next == None:
            self.head = None
        else:
            prev=None
            temp=self.head
            while temp.next != None:
                prev=temp
                temp=temp.next
            prev.next=None

    def deleteByValue(self,value):
        if self.head == None:
            print("empty list")
        elif self.head.data==value:
            self.head=self.head.next
        else:
            prev=None
            temp=self.head
            while temp != None and temp.data != value:
                prev=temp
                temp=temp.next
            if temp == None:
                print("value not found")
            else:
                prev.next=temp.next

    def alter(self):
        temp=self.head
        if self.head == None:
            print("empty list")
        while temp != None:
            print(temp.data,end=" ")
            temp=temp.next.next
        print()



sll=SLL()
print("linked list elements are:")
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.print()

# sll.InsertAnyPos(30,2)
# sll.print()

# sll.deleteAtFirst()
# sll.print()

# sll.deleteAtLast()
# sll.print()

# sll.deleteByValue(20)
# sll.print()

# sll.deleteByValue(1)
# sll.print()

sll.alter()

