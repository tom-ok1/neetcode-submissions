class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for str in strs:
            for c in str:
                if c == "," or c == "\\":
                    encoded += "\\"
                encoded += c
            encoded += ","
        return encoded

    def decode(self, s: str) -> List[str]:
        tmp_str = ""
        ans = []
        i = 0
        while i < len(s):
            if s[i] == "\\":
                i += 1
                tmp_str += s[i]
            elif s[i] == ",":
                ans.append(tmp_str)
                tmp_str = ""
            else:
                tmp_str += s[i]

            i += 1
        return ans

