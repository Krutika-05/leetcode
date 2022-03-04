class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=''
        for i in list(zip(*strs)): #If you use zip() with n arguments, then the function will return an iterator that generates tuples of length n.
            if len(set(i))==1:
                prefix=prefix+i[0]
            else:
                break
        return prefix
        """
        :type strs: List[str]
        :rtype: str
        """
        