class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1: (2, 3) or (3, 2)
            # 2: 3
            # 3: 2
        # [1,2,3,4]
        # 1: (2,3,4)
            # 2: (3, 4), (4, 3)
                # 3: (4)
                    # 4: none -> add this permutation and return
                # 4: (3)
            # 3: 
            # 4: 
        # 2: (1,3,4) -> q(2)
            # loop
                # compare 1 with q[1]
                # dfs(q[2, 1])
        ans = []
        def dfs(s, acc):
            if len(acc) == len(nums):
                ans.append(acc[:])
                return
            for num in nums:
                if num in s:
                    continue

                s.add(num)
                acc.append(num)
                dfs(s, acc)
                s.remove(num)
                acc.pop()
        dfs(set(), [])
        return ans