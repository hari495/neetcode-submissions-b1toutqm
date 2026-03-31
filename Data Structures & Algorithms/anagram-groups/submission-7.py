class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        
        for s in strs:
            freq=[0]*26
            for char in s:
                freq[ord(char)-ord('a')]+=1
            
            key=tuple(freq)
            group[key].append(s)
        return list(group.values())