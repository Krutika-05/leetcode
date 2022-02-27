class Solution(object):
    def uniqueOccurrences(self, arr):
        occList = []
        unique_list = list(set(arr))
        for i in unique_list:
            c= arr.count(i)
            occList.append(c)
        occList.sort()
        for i in range(len(occList)):
            for j in range(i+1, len(occList)):
                if occList[i] == occList[j]:
                    return False
        return True
    
    # def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
      