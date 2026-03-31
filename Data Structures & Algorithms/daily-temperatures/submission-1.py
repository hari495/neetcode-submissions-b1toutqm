class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_to_wait=[0]*len(temperatures)
        stack=[]

        for i, today_temp in enumerate(temperatures):
            while stack and today_temp > temperatures[stack[-1]]:
                j=stack.pop()
                days_to_wait[j] = i-j
            stack.append(i)
        return days_to_wait
