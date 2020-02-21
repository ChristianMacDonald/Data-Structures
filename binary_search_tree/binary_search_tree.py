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
        while True:
            if current_node.value > value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BinarySearchTree(value)
                    break
            elif current_node.value <= value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BinarySearchTree(value)
                    break
        


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node = self
        while True:
            if current_node.value > target:
                if current_node.left:
                    current_node = current_node.left
                else:
                    return False
            elif current_node.value < target:
                if current_node.right:
                    current_node = current_node.right
                else:
                    return False
            else:
                return True

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while True:
            if current_node.right:
                current_node = current_node.right
            else:
                return current_node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)
