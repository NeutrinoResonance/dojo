from typing import List
from functools import reduce
import pdb

class Solution(object):
    def reverse_slice(self, start_idx: int, end_idx: int, array: List[int]) -> None:
        length = end_idx - start_idx + 1
        mid = int(length / 2)
        
        for i in range(0, mid):
            lo = start_idx + i
            hi = start_idx + length - i - 1
            
            self.swap(lo, hi, array)


    def swap(self, source: int, dest: int, array: List[int]) -> None:
        temp = array[source]
        array[source] = array[dest]
        array[dest] = temp
        # This is the original array, just mutated
        # return array
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for i in reversed(range(len(nums))):
            # If this is the case we have an already reversed list
            if (i - 1) < 0 :
                nums.reverse()
                break

            if nums[i-1] < nums[i]:
                # Find nums[j] such that nums[j] is minimally larger than nums[i-1]
                min_dist = nums[i] - nums[i-1]
                min_num = nums[i-1]
                j_idx = i
                
                for j in range(i, len(nums)):
                    if nums[j] <= nums[i - 1]:
                        continue
                    
                    new_dist = nums[j] - nums[i-1]

                    assert(new_dist >= 0)

                    if (new_dist <= min_dist):
                        min_dist = new_dist
                        min_num = nums[j]
                        j_idx = j

                self.swap(i-1, j_idx, nums)
                # self.swap(i, j_idx, nums)
                # ^^ Incorrect - i-1 is the one that needs to be 'upped'
                # print("after swap, before reverse: %s" % str(nums))
                # pdb.set_trace()
                
                if i < len(nums)-1:
                    self.reverse_slice(i, len(nums)-1, nums)
                # ^^ and the rest of the string needs to be kicked down to get
                # only the /next/ greatest lexicographic permutation, not anything greater!
                break
                
        return nums
