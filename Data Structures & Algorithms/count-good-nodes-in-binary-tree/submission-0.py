# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([root])
        ans = 1
        while q:
            next_q = deque()
            print(f"len: {len(q)}")
            for _ in range(len(q)):
                parent = q.popleft()
                print(parent.val)
                if parent.left:
                    if parent.left.val >= parent.val:
                        ans += 1
                    else:
                        parent.left.val = parent.val
                    next_q.append(parent.left)
                if parent.right:
                    if parent.right.val >= parent.val:
                        ans += 1
                    else:
                        parent.right.val = parent.val
                    next_q.append(parent.right)

            q = next_q
        return ans