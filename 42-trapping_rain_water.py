class Solution(object):
    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        contributions = [0]*len(heights)

        for (index, height) in enumerate(heights):
            if index == 0:
                continue

            i = index - 1

            max_height = 0
            contribution = 0
            while (i >= 0) and (max_height < height):
                current = heights[i]

                distance = (index - i) - 1
                if current != 0 and current > max_height and distance != 0:
                    new_area_height = min(current, height) - max_height

                    assert distance > 0
                    new_area = new_area_height * distance

                    contribution += new_area

                max_height = max(max_height, current)

                i -= 1

            contributions[index] = contribution

        return sum(contributions)
