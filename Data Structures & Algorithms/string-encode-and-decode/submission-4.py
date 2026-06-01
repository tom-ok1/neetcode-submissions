class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s):03d}{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        pos = 0
        ans = []
        while pos < len(s):
            len_s = int(s[pos : pos + 3])
            pos += 3
            payload = s[pos : pos + len_s]
            ans.append(payload)
            pos += len_s
        return ans