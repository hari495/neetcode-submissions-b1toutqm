class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl=0
        substr=""
        for c in s:
            if c not in substr:
                substr+=c
            elif c==substr[0]:
                substr=substr[1:]
                substr+=c
            else:
                substr=c
            maxl=max(maxl,len(substr))
        return maxl