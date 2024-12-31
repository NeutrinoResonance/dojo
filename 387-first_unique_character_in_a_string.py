class Solution(object):
    def firstUniqChar(self, s):
        if len(s) == 0:
            return -1
        
        # letter -> (first occurrence index, number of times occurred)
        count = {}

        winner_idx = None
        winner_char = None

        for (index, i) in enumerate(s):
            params = count.setdefault(i, [0, 0])
            if params[0] == 0:
                params[0] = index
            params[1] += 1

        lowest_idx = None
        for (char, params) in count.iteritems():
            (first_idx, char_count) = params
            if char_count == 1:
                if lowest_idx is None:
                    lowest_idx = first_idx
                else:
                    if lowest_idx > first_idx:
                        lowest_idx = first_idx
        return -1 if lowest_idx is None else lowest_idx
