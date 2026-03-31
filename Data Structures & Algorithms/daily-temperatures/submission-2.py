class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_to_wait=[0]*len(temperatures)
        stack=[]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                s=stack.pop()
                days_to_wait[s[0]]=i-s[0]
            stack.append([i,temp])

        return days_to_wait