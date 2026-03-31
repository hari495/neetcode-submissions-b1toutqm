class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[[p,s] for p,s in zip(position,speed)]
        stack=[]

        for pair in sorted(pairs,reverse=True):
            t=(target-pair[0])/pair[1]
            stack.append(t)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)