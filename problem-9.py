class Solution:
    def reorderSpaces(self, text: str) -> str:
        ans = ""
        ws_count = text.count(' ')
        words_list = text.split()
        word_count = len(words_list)
        if word_count == 1:
            ans = words_list[0] + ws_count*" "
            return ans
        space_length = ws_count // (word_count-1)
        s = " "*space_length
        ans = s.join(words_list) + " "*(ws_count%(word_count-1))
        return ans










