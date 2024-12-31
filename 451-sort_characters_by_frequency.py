class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        frequency = {}
        builder = []

        for i in s:
            count = frequency.setdefault(i, 0)
            count += 1
            frequency[i] = count

        for item in reversed(sorted(frequency.items(), key = lambda x: x[1])):
            # print item 
            char, count = item
            print i
            for i in range(0, count):
                builder.append(char)

        value = "".join(builder)

        return value
