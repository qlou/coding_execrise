preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

# Define a tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def helper(in_left=0, in_right=len(inorder)):
            nonlocal pre_idx
            if in_left == in_right:
                return None

            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            index = idx_map[root_val]

            pre_idx += 1
            root.left = helper(in_left, index)
            root.right = helper(index + 1, in_right)
            # print(root.val)
            return root

        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        # print(idx_map)
        return helper()
# idx_map = {val:idx for idx, val in enumerate(inorder)}
# print(enumerate(inorder))
#print(idx_map)

s = Solution()

print(s.buildTree(preorder,inorder).val)