class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_count = 0
        increased_string = word
        while True:
            if increased_string in sequence:
                max_count +=1
                increased_string +=word
            else:
                break
        return max_count









