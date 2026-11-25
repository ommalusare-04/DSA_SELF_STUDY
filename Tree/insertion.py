# class Node:
#     def __init__(self,value):
#         self.left=None
#         self.data=value
#         self.right=None

# class BST:
#     def __init__(self):
#         self.root=None
#     def insert(self,newnode):
#         if self.root is None:
#             self.root=newnode
#         else:
#             temp=self.root
#             while True:
#                 if newnode.data < temp.data:
#                     if temp.left is None:
#                         temp.left=newnode
#                         return
#                     else:
#                         temp=temp.left
                        
#                 else:
#                     if temp.right is None:
#                         temp.right=newnode
#                         return
#                     else:
#                         temp=temp.right
                        

#     def Inorder(self,rt):
#         if rt is None:
#             return
#         else:
#             self.Inorder(rt.left)
#             print(rt.data,end=" ")
#             self.Inorder(rt.right)

# b=BST()
# b.insert(Node(45))
# b.insert(Node(4))
# b.insert(Node(5))
# b.insert(Node(453))
# b.insert(Node(55))
# b.insert(Node(89))

# b.Inorder(b.root)


c