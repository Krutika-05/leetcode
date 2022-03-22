class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
            if len(nums) == len((set(nums))) :
                return False
            return True
         # Alternative - using counter   
        # count = Counter(nums)
        # for i in count:
        #     if count[i] > 1:
        #         return True
        # return False
    

        