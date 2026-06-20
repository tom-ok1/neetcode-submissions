class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []
        def list_combination(idx, path):
            print(idx)
            for char in phone[digits[idx]]:
                cur_path = path + char
                print(cur_path, path)
                if len(cur_path) == len(digits):
                    ans.append(cur_path)
                else:
                    list_combination(idx + 1, cur_path)

        list_combination(0, "")
        return ans