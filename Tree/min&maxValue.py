
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,newnode):
        if self.root == None:
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

    def inorder(self,rt):
        if rt == None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)

    def preorder(self,rt):
        if rt == None:
            return
        else:
            print(rt.data,end=" ")
            self.preorder(rt.left)   
            self.preorder(rt.right)  

    def postorder(self,rt):
        if rt == None:
            return
        else:
            self.postorder(rt.left)   
            self.postorder(rt.right) 
            print(rt.data,end=" ")

    def MinMax(self):
        temp=self.root
        if temp == None:
            print("empty tree")
        while temp.left != None:
            temp=temp.left
        print("Minimum value:",temp.data)

        temp=self.root
        while temp.right != None:
            temp=temp.right
        print("Maximum Value:",temp.data)



b=BST()
b.insert(Node(12))
b.insert(Node(1))
b.insert(Node(72))
b.insert(Node(2))

print("Inorder traversal:")
b.inorder(b.root)

print("\nPreorder traversal:")
b.preorder(b.root)

print("\nPostorder traversal:")
b.postorder(b.root)

print()

b.MinMax()