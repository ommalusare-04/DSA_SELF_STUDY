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
            self.head=newnode
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp

    def deletebykey(self, data):
        temp = self.head
        prev = None

        while temp is not None:
            if temp.data == data:  
                if prev is not None:
                    prev.next = temp.next  
                else:
                    self.head = temp.next  

                if temp.next is not None:
                    temp.next.prev = prev  
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
    
    def traveersal(self):
        if self.head==None:
            print("empty list")
        else:
            temp=self.head
            while temp.next != None:
                print(temp.data,end=" ")
                temp=temp.next
            print(temp.data)

dll=DLL()
dll.append(10)
dll.append(20)
dll.append(10)
dll.append(200)
dll.traveersal()

dll.deletebykey(200)
dll.traveersal()

