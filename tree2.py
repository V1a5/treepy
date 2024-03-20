class node :
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data is None:
            self.data = data
        else :
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data,end=" ")
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data,end=" ")
        

root = node('g')
root.insert('c')
root.insert('b')
root.insert('e')
root.insert('a')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('j')
root.insert('h')
root.insert('k')

print("Preorder   :",end=" ")
root.preorder()
print("\nInorder    :",end=" ")
root.inorder()
print("\nPostorder  :",end=" ")
root.postorder()

