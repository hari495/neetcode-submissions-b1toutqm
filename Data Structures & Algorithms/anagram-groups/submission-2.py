class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for string in strs:
            map=[0]*26
            for char in string:
                map[ord(char)-ord('a')]+=1
            key=tuple(map)
            if key in group:
                group[key].append(string)
            else:
                group[key]=[string]
        return list(group.values())
