import pdb

def container_area(left_idx, right_idx, heights):
    if left_idx == right_idx:
        return 0
    
    left_height, right_height = heights[left_idx], heights[right_idx]
    
    width = right_idx - left_idx

    min_height = min([left_height, right_height])
    
    return width * min_height
    
class Solution(object):
    def __init__(self):
        self.best_left_idx = None
        self.best_right_idx = None
        self.best_area = 0
        
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        memo = {}

        left_idx = 0
        right_idx = len(heights)-1

        for i in range(0, len(heights)):
            left_height = heights[left_idx]
            
            right_height = heights[right_idx]
            # pdb.set_trace()

            area = container_area(left_idx, right_idx, heights)
            if area > self.best_area:
                self.best_left_idx = left_idx
                self.best_right_idx = right_idx
                self.best_area = area
            
            if left_height <= right_height:
                left_idx += 1
                if left_idx > right_idx or left_idx >= len(heights):
                    return self.best_area
                
            elif right_height < left_height:
                right_idx -= 1
                if right_idx < left_idx or right_idx <= 0:
                    return self.best_area
            
        return self.best_area


def test(heights, target=None):
    sol = Solution()
    max_area = sol.maxArea(heights)
    
    print("Found %d with index/height pairs: left (idx:%d, height:%d) right (idx:%d, height:%d)" % (max_area,
                                                                          sol.best_left_idx,
                                                                          heights[sol.best_left_idx],
                                                                          sol.best_right_idx,
                                                                          heights[sol.best_right_idx]))
    
    if target != None:
        print("\ttarget: %d" % target)
        
if __name__ == "__main__":
    test([1,8,6,2,5,4,8,3,7], 49)
