# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([root])
        ans = []
        while q:
            cur_q = deque()
            next_q = deque()
            for _ in range(len(q)):
                node = q.popleft()
                cur_q.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            ans.append(list(cur_q))
            q = next_q
        return ans