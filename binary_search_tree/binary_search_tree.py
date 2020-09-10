"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else: self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        else:
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #base case
        #if tree is empty return none
    #while there is a right child, move to the right
    #once there are no more right children, return the value
        if not self:
            return None

        while self.right:
            self = self.right

        return self.value

    def get_min(self):
        # if tree is empty return none
        # while there is a left child, move to the left
        # once there are no more left children, return the value
        if not self:
            return None

        while self.left:
            self = self.left

        return self.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #call foreach on the root node
        # if left exists call for each on the left child
        # if right exists call for each on the right child
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        visited = []
        queue = []
        #grab starting node
        node = self.root
        #put the starting node in the queue
        queue.insert(0, self.root)# root or head

        while queue.len:
            node = queue.pop(0)
            visited.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return visited

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        visited = []
        current = self.root

        def traverse(self, node):
            visited.append(self.node.value)
            if node.left:
                traverse(self.node.left)
            if node.right:
                traverse(self.node.right)

        traverse(current)
        return visited



    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
