class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        
        for s in strs:
            freq=[0]*26
            for char in s:
                freq[ord(char)-ord('a')]+=1
            
            key=tuple(freq)
            if key in group:
                group[key].append(s)
            else:
                group[key]=[s]
        return list(group.values())