import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        current_node = self
        print("current_node", current_node.value)
        #If inserting we must a already have a tree or root.
        # If value less than the self.value self.left, make a new tree/node if empty, otherwise
        # keep going (recursion)
        if current_node.value > value:
            if current_node.left is None:
                current_node = BinarySearchTree(value)
                return
            current_node = current_node.left




        # if value greater than or equal to then go right, make new tree/node if empty, otherwise
        #keep going
        elif current_node.value <= value:
            if current_node.right is None :
                current_node = BinarySearchTree(value)
                return
            current_node = current_node.right


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target = self.value, otherwise
        # go left or right
           pass

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, got right
        # otherwise return self.value

        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
