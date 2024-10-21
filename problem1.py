# time: O(n)
# space: O(w) w is the width of the tree
# leetcode 515. Find Largest Value in Each Tree Row

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        # dfs
        # hmap = defaultdict(list)
        # result = []
        
        # def helper(node, level):
        #     if not node:
        #         return
            
        #     hmap[level].append(node.val)

        #     helper(node.left, level+1)
        #     helper(node.right, level+1)
        
        # helper(root, 0)

        # for level in range(len(hmap)):
        #     result.append(max(hmap[level]))
        # return result

        # bfs
        res = []
        queue = deque([root])

        while queue:
            rowmax = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()

                rowmax = max(rowmax, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(rowmax)
        return res