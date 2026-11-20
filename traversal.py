class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,newnode):
        if self.root is None:
            self.root=newnode
        else:
            temp=self.root
            while True:
                if newnode.data < temp.data:
                    if temp.left is None:
                        temp.left=newnode
                        return
                    else:
                        temp=temp.left

                else:
                    if temp.right is None:
                        temp.right=newnode
                        return
                    else:
                        temp=temp.right

    def Inorder(self,rt):
        if rt is None:
            return
        else:
            self.Inorder(rt.left)
            print(rt.data,end=" ")
            self.Inorder(rt.right)

    def Preorder(self,rt):
        if rt is None:
            return
        else:
            print(rt.data,end=" ")
            self.Inorder(rt.left)
            self.Inorder(rt.right)

    def POstorder(self,rt):
        if rt is None:
            return
        else:
            
            self.Inorder(rt.left)
            self.Inorder(rt.right)
            print(rt.data,end=" ")

d=BST()
d.insert(Node(12))  
d.insert(Node(2)) 
d.insert(Node(123)) 
d.insert(Node(25)) 
d.insert(Node(62)) 
d.insert(Node(1))   

print("Inorder Traversal:")
d.Inorder(d.root)
print()
print("Preorder Traversal Traversal:")
d.Preorder(d.root)
print()
print("Postorder Traversal Traversal:")
d.POstorder(d.root)