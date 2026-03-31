class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for string in strs:
            freq_map=[0]*26
            for char in string:
                freq_map[ord(char)-ord('a')]+=1
            key=tuple(freq_map)
            if key in group:
                group[key].append(string)
            else:
                group[key]=[string]
        return list(group.values())
            