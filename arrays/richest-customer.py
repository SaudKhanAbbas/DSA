class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximumWealth = 0 
        for customer in accounts:
            currentWealth = 0 
            for money in customer:
                currentWealth = currentWealth + money 

            if currentWealth>maximumWealth:
                maximumWealth = currentWealth
        
        return maximumWealth
