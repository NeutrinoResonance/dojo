class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return None
        
        for (index, i) in enumerate(reversed(range(0, m))):
            nums1[len(nums1)-index-1] = nums1[i]
            nums1[i] = 0
            
        one_idx = len(nums1) - m
        two_idx = 0
        
        for current_idx in range(0, len(nums1)):
            one_candidate = nums1[one_idx] if one_idx < len(nums1) else None
            two_candidate = nums2[two_idx] if two_idx < len(nums2) else None
            
            winner = None
            assert not (one_candidate == None and two_candidate == None)
            if one_candidate == None:
                winner = 2
                
            if two_candidate == None:
                winner = 1
                
            if winner == None:
                if one_candidate < two_candidate:
                    winner = 1
                elif two_candidate < one_candidate:
                    winner = 2
                else:
                    # Arbitrarily break the tie - this isn't the only strategy
                    assert one_candidate == two_candidate
                    winner = 1
            
            value = None
            if winner == 1:
                value = nums1[one_idx]
                one_idx += 1
            else:
                value = nums2[two_idx]
                two_idx += 1
                
            nums1[current_idx] = value 
            
        return None
