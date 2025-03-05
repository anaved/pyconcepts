'''
Created on Feb 5, 2014

@author: Naved
'''
class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BTree(object):
    def __init__(self):
        self.root=None
    def insert(self,value):
        if not self.root:
            self.root=Node(value)                
        else:
            self.insert_recursive(self.root,value)

    def insert_recursive(self,node,value):
        if value < node.value:
            if node.left==None:
                node.left=Node(value)
            else:
                self.insert_recursive(node.left,value)                
        else:
            if node.right==None:
                node.right=Node(value)
            else:
                self.insert_recursive(node.right,value)

    def traverse(self,node):
        if node:
            self.traverse(node.left)
            print(node.value,"--")
            self.traverse(node.right)                    
tree=BTree()
[tree.insert(e) for e in  [100,2,3,3,4,5,6,7,8,99,99]]
tree.traverse(tree.root)
