import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        # n time complexity
        def can_eat_up(k):
            count = 0
            for pile in piles:
                count += math.ceil(pile / k)
                if count > h:
                    return False
            return True
        # 1,2,3,4
        # left is 1, right is 4, mid is 2
        # 2 is true, right is 1
        # left = right, this doesn't meet the condition => fail
        left, right = 1, piles[-1]
        ans = piles[-1]
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if can_eat_up(mid):
                print("true")
                ans = mid
                right = mid - 1
            else:
                print("false")
                left = mid + 1
        return ans