class Solution:
    def encode(self, strs: List[str]) -> str:
        # receive strings and seperate them with some symbol like #
        # string structure will be like | size of value1 | value1 | size of value2 | value2 | ...
        return "".join([f"{len(s):03}{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        # split s by #
        offset = 0
        ans = []
        while offset < len(s):
            size = int(s[offset:offset+3])
            offset += 3
            value = s[offset:offset+size]
            offset += size
            ans.append(value)
        return ans