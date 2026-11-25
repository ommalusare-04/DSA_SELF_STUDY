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
                    if temp.left == None:
                        temp.left = newnode
                        return
                    else:
                        temp=temp.left

                else:
                    if temp.right == None:
                        temp.right = newnode
                        return
                    else:
                        temp=temp.right

    def Inorder(self,rt):
        if rt == None:
            return
        else:
            self.Inorder(rt.left)
            print(rt.data,end=" ")
            self.Inorder(rt.right)

b=BST()
b.insert(Node(34))
b.insert(Node(4))
b.insert(Node(78))
b.insert(Node(94))

b.Inorder(b.root)