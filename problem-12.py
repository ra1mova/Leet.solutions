class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles<numExchange:
            return numBottles
        elif numBottles==numExchange:
            return numBottles+1
        else:
            
            c=0
            while numBottles>=numExchange:
                numBottles = numBottles-numExchange+1
                c+=1
            return c*numExchange+numBottles













