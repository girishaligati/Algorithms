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
        # print(node_q)
        # print(type(node_q))
        self.__add(node_q[0],node_q,key,0)
        del node_q
    
    def __add(self,temp_node,node_q,key,index):
        if temp_node.left == None:
            temp_node.left = Node(key)
            return
        elif temp_node.right == None:
            temp_node.right = Node(key)
            return
        else:
            node_q.append(temp_node.left)
            node_q.append(temp_node.right)
            index = index + 1
            self.__add(node_q[index],node_q,key,index)
    
    def in_order(self,node):
        self.__in_order(node)
    
    def __in_order(self,node):
        if(node == None):
            return
        else:
            self.in_order(node.left)
            print(node.key)
            self.in_order(node.right)
    
    def find(self,key):
        node_q= [BinaryTree.root]
        key_at = []
        index = 0
        self.__find(node_q[index],node_q,key,index,key_at)
        if key_at:
            print("Key Found",key_at)
        else:
            print("Key Not Found")

    def __find(self,temp_node,node_q,key,index,key_at):
        if temp_node != None:
            if temp_node.key == key:
                key_at.append(temp_node)
            else:
                if temp_node.left != None:
                    node_q.append(temp_node.left)
                if temp_node.right != None:
                    node_q.append(temp_node.right)
                index = index + 1
                if index < len(node_q):
                    self.__find(node_q[index],node_q,key,index,key_at)
    
    # def level_traversal(self):
    #     node_q = [BinaryTree.root]
    #     index = 0
    #     self.__level_traversal(node_q[index],node_q,index)
    #     print(node_q)
    #     for i in node_q:
    #         print(i.key)
    
    # def __level_traversal(self,temp_node,node_q,index):
    #     if temp_node != None:
    #         if temp_node.left != None:
    #             node_q.append(temp_node.left)
    #         if temp_node.right != None:
    #             node_q.append(temp_node.right)
    #         index = index + 1
    #         if index < len(node_q):
    #             return self.__level_traversal(node_q[index],node_q,index)
    
    # def delete(self,key):
    #     node_q = [BinaryTree.root]
    #     self.__level_traversal(node_q[0],node_q,0)
