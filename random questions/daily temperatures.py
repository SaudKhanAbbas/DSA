class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = []

        for i in range(n):
            days = 0
            found = False

            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    days = j-i
                    found = True
                    break
            
            if found:
                answer.append(days)
            else:
                answer.append(0)
        
        return answer
        
