class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        check = [[0, 0]]
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            elif i == 'W':
                x -= 1
            if [x, y] in check:
                return True
            check.append([x, y])
        return False











