class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        l=len(nums)

        po=0



        for i in range(l-1):

            if nums[po+1] !=nums[po]:     

                po += 1

            else:

                nums.remove(nums[po])

        return len(nums)
