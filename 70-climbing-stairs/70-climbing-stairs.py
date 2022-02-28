class Solution(object):
    def climbStairs(self, n):
        previous, current = 0, 1
        for i in range(n):
            previous, current = current, previous + current    
        return current
        """
        :type n: int
        :rtype: int
        """
    