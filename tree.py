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

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def preorder(root):
    print(root.data)
    preorder(root.left)
    preorder(root.right)

if __name__=='__main__':
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

inorder(root)