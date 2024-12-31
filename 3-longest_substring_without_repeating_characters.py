class Solution(object):
    def __init__(self):
        self.best_length = 0
        self.best_start_idx = 0
        
    def get_best_substring(self, s):
        return s[self.best_start_idx:self.best_start_idx+self.best_length]
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # None, not zero since we may have a string of length 0 - it is not
        # logical that an empty string will have any indicies at all
        # best_start_idx = None
        # best_end_idx = None

        
        if len(s) == 0:
            return 0

        # letter -> last location (index)
        # NOT A SET
        seen = {}

        start_idx = 0
        current_length = 0
        current_idx = 0
        
        while current_idx < len(s):
            char = s[current_idx]

            if current_length > self.best_length:
                self.best_length = current_length
                self.best_start_idx = start_idx

            if char in seen:
                # Terminate the current sequene
                start_idx = seen[char]
                current_idx = seen[char]
                current_length = 0
                
                seen.clear()
            else:
                current_idx += 1
                current_length += 1
                seen[char] = current_idx
            
            # else:
        
        if current_length > self.best_length:
            self.best_length = current_length
            self.best_start_idx = start_idx

        return self.best_length
