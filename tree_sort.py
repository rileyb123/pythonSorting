


class Node:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self,val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

def inorder(root , arr):
    if root:
        inorder(root.left,arr)
        arr.append(root.val)
        inorder(root.right,arr)

def tree_sort(arr):

    if len(arr) == 0:
        return []
    root = Node(arr[0])
    for i in range(1,len(arr)):
        root.insert(arr[i])

    ret = []
    inorder(root, ret)
    return ret
            