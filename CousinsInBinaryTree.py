'''In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.'''

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return false
        
        stack = [[root, 0, -1]]
        
        cousin_1 = []
        cousin_2 = []
        
        while stack:
            node, h, parent = stack.pop()
            
            # find cousins
            if node.val == x: cousin_1 = [h, parent]
            if node.val == y: cousin_2 = [h, parent]
            
            if node.right: stack.append([node.right, h+1, node.val])
            if node.left: stack.append([node.left, h+1, node.val])
        
        if cousin_1[0] == cousin_2[0] and cousin_1[1] != cousin_2[1]:
            return True
        return False
        