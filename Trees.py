class Node(object):
    def __init__ (self,key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree(object):
    root = None
    def __init__(self,key):
        if BinaryTree.root == None:
            BinaryTree.root = Node(key)
        else:
            self.add(key)
    
    def add(self,key):
        node_q= [BinaryTree.root]
        print(node_q)
        print(type(node_q))
        self.__add(node_q[0],node_q,key)
        del node_q
    
    def __add(self,temp_node,node_q,key):
        if temp_node.left == None:
            temp_node.left = Node(key)
            return
        elif temp_node.right == None:
            temp_node.right = Node(key)
            return
        else:
            node_q.append(temp_node.left)
            node_q.append(temp_node.right)
            self.__add(node_q[1],node_q[1:],key)
    
    def in_order(self,node):
        self.__in_order(node)
    
    def __in_order(self,node):
        if(node == None):
            return
        else:
            self.in_order(node.left)
            print(node.key)
            self.in_order(node.right)
