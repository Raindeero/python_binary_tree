class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        '''
        Function inserts value into binary tree
        :param data:
        :return:
        '''
        if self.data:
            if self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            # if number is equal or bigger than node
            else:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data

    def preorder_traversal(self):
        '''
        preorder traversal through tree: print root -> left sub-tree -> right sub-tree
        :return:
        '''
        if self.data is not None:
            print(self.data)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def inorder_traversal(self):
        '''
        inorder traversal through tree: print left sub-tree -> root -> right sub-tree
        :return:
        '''
        if self.left:
            self.left.inorder_traversal()
        if self.data is not None:
            print(self.data)
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        '''
        postorder traversal through tree: print left sub-tree -> right sub-tree -> root
        :return:
        '''
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        if self.data is not None:
            print(self.data)

    def find_value(self, value):
        '''
        search function value in tree
        :param value:
        :return: message "{value} is found" or "{value} not found"
        '''
        if value < self.data:
            if self.left is None:
                print(f"{value} not found")
                return 1
            return self.left.find_value(value)
        elif value > self.data:
            if self.right is None:
                print(f"{value} not found")
                return 1
            return self.right.find_value(value)
        else:
            print(f"{value} is found")


# delete tree
def del_tree(root):
    '''
    Deleting tree by node that given in params
    :param root:
    :return:
    '''
    if root is None:
        return
    del_tree(root.left)
    del_tree(root.right)
    root.data = None
    root.left = None
    root.right = None


def del_node_by_data(root, value):
    '''
    Find and delete (sub-tree)/list/(whole tree) by value
    :param root:
    :param value:
    :return:
    '''
    if root is None:
        return
    if root.data < value:
        del_node_by_data(root.right, value)
    elif root.data > value:
        del_node_by_data(root.left, value)
    else:
        del_tree(root)


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.preorder_traversal()
print(" next")
root.inorder_traversal()
print(" next")
root.postorder_traversal()
root.find_value(31)
root.find_value(23462)

# root.inorder_traversal()
# # del_tree(root)
# print("delete 14")
# del_node_by_data(root, 14)
# root.inorder_traversal()
