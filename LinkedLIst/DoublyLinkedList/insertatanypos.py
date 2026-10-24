
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

    def insertathead(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def insertat(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return  
        if pos == 1:
            self.insertathead(data)  
            return  
        
        newnode = Node(data)
        temp = self.head
        count = 1
        
        while temp != None and count < pos -1:
            temp = temp.next
            count += 1
        if temp == None:
            print("Invalid position")  
            return
        newnode.next = temp.next  
        newnode.prev = temp       
        if temp.next != None:
            temp.next.prev = newnode 
        temp.next = newnode  


    def traversal(self):
        if self.head == None:
            print("Empty list")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
            print()


dll1 = DLL()

dll1.append(10)
dll1.append(20)
dll1.append(30)

print("Original list:")
dll1.traversal()

dll1.insertat(15, 2)

print("After inserting 15 at position 2:")
dll1.traversal()
