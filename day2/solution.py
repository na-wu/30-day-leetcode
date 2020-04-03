class Solution:
    def isHappy(self, n:int):

        while n != 1:
            if n == 4:
                return False
            res = 0
            x = str(n)
            for i in x:
                res += int(i)**2
            n = res
        return True