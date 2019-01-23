# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_BST(root, Min, Max):
    
    if not root: return True # Base Case
    
    if root.data <= Min or root.data >= Max: return False
    
    return check_BST(root.left, Min, root.data) and check_BST(root.right, root.data, Max)
    
    
def checkBST(root):
    return check_BST(root,-1,10001)
    
    
    
    # Failed Solution 1: 12/15 test cases passed
    # ---------------------------------------
#     def inorder(root,l):
#         if root:
#             inorder(root.left,l)
#             l.append(root.data)
#             inorder(root.right,l)   
#         return l
    
#     l = inorder(root,[])
#     #print(l)
    
    ## The problem here is with repeating consecutive numbers in the inorder list
    ## iteratively checking the sort in the below line might solve the problem
#     if (l == sorted(l)): return True
#     else: return False

        
