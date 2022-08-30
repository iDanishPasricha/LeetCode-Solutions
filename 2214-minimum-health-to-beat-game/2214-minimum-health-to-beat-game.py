class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage)+1 - min(max(damage), armor)
        
        
'''
You will only get one shot, so pick the turn that you may lose the most health
Your total loss-avoidable will be min(max(damage), armor)
You will need at least sum(damage) + 1 to pass the game without any armor

'''