class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dict_t={}
        for c in t:
            dict_t[c]=dict_t.get(c,0)+1
        
        need=len(dict_t)

        window_counts={}

        have=0
        min_len=float("inf")
        res=[0,0]
        l=0

        for r in range(len(s)):
            char=s[r]
            window_counts[char]=window_counts.get(char,0)+1

            if char in dict_t and window_counts[char]==dict_t[char]:
                have+=1

            while have==need:
                if r-l+1<min_len:
                    min_len=r-l+1
                    res=[l,r]
                
                
                window_counts[s[l]]-=1
                if s[l] in dict_t and window_counts[s[l]]==dict_t[s[l]]-1:
                    have-=1
                
                l+=1

        return s[res[0]:res[1]+1] if min_len!=float("inf") else ""
