import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # iterative solution
    # Insert the given value into the tree
    # def insert(self, value):
    #
    #     current_node = self
    #            #If inserting we must a already have a tree or root.
    #     # If value less than the self.value self.left, make a new tree/node if empty, otherwise
    #     # keep going (recursion)
    #     while current_node:
    #         if current_node.value > value:
    #             if current_node.left is None:
    #                 current_node.left = BinarySearchTree(value)
    #                 return
    #             current_node = current_node.left
    #
    #
    #
    #
    #     # if value greater than or equal to then go right, make new tree/node if empty, otherwise
    #     #keep going
    #         elif current_node.value <= value:
    #             if current_node.right is None:
    #                 current_node.right = BinarySearchTree(value)
    #                 return
    #             current_node = current_node.right
    # recursive solution
    def insert(self, value):
            if value > self.value:
                if self.right is not None:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
            else:
                if self.left is not None:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    # iterative
    # def contains(self, target):
    #     current_node = self
    #
    #     # if target = self.value, otherwise
    #     # go left or right
    #     while current_node:
    #         if target == current_node.value:
    #             return True
    #         elif target > current_node.value:
    #             if current_node.right is None:
    #                 return False
    #             current_node = current_node.right
    #         elif target < current_node.value:
    #             if current_node.left is None:
    #                 return False
    #             current_node = current_node.left
    # recursive solution
    def contains(self, target):
            if target == self.value:
                return True
            if target > self.value and self.right is not None:
                return self.right.contains(target)
            elif target < self.value and self.left is not None:
                return self.left.contains(target)
            else:
                return False


    # Return the maximum value found in the tree
    # iterative solution
    # def get_max(self):
    #     # if right exists, got right
    #     # otherwise return self.value
    #     current_node = self
    #     while current_node.right is not None:
    #
    #
    #             current_node = current_node.right
    #     return current_node.value
    # recursive solution
    def get_max(self):
            if self.right is not None:
                return self.right.get_max()
            else:
                return self.value



    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        current_node = self
        cb(current_node.value)
        if current_node.left is not None:
            current_node.left.for_each(cb)
        if current_node.right is not None:
            current_node.right.for_each(cb)


    # DAY 2 Project -----------------------
    #Steps
    # Make a Stack
    # put root in stack
    # while stack is not empty
    #     pop root out of stack
    #     if left
    #       add left to stack
    #     if right
    #       add right to stack
    # Breath First Travseral
    # Make a queue
    # Put root in the queue
    # while queue is not empty
    #    pop out fron of queue
    #    Do the thing
    #    if left
    #      add left to back of queue
    #    if right
    #      add right to back of queue

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self)
        print(self.value)
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        current_node = node
        while current_node:
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
            current_node = queue.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
