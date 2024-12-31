class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        def helper(node, lower_bound=None, upper_bound=None):
            valid = True
            if lower_bound != None:
                valid &= node.val > lower_bound
                
            if upper_bound != None:
                valid &= node.val < upper_bound

            if valid:
                if node.right != None:
                    next_lower_bound = node.val if lower_bound == None else max(node.val, lower_bound)
                    valid &= helper(node.right, next_lower_bound, upper_bound)
                if node.left != None:
                    next_upper_bound = node.val if upper_bound == None else min(node.val, upper_bound)
                    valid &= helper(node.left, lower_bound, next_upper_bound)
            return valid 
                
        return helper(root)
