from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_cnt_dict = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(s)):
            char_cnt_dict[s[right]] += 1
            if char_cnt_dict[s[right]] > 1:
                ans = max(ans, right - left)
                while char_cnt_dict[s[right]] > 1:
                    char_cnt_dict[s[left]] -= 1
                    left += 1
        return max(ans, len(s) - left)