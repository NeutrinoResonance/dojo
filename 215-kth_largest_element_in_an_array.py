import math

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numbers = nums
        
        if numbers == None:
            return None
        if len(numbers) == 0:
            return None

        assert k in range(1, len(numbers)+1)

        # We assume sort is n*log(n), so if we have
        # to do more iterations than this we can just
        # sort and index
        if k > math.ceil(math.log(len(numbers), 2)):
            numbers.sort()
            return numbers[len(numbers) - k]
        else:
            current_max = None
            max_index = None

            for i in range(0, k):
                for (index, j) in enumerate(numbers):
                    if j == None:
                        pass

                    if current_max == None:
                        current_max = j
                        max_index = index
                    else:
                        if j > current_max:
                            current_max = j
                            max_index = index

                numbers[max_index] = None

                if i != k-1:
                    current_max = None
                    max_index = None

            return current_max
