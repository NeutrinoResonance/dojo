class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        closes = {"(": ")",
                  "[": "]",
                  "{": "}"}
        opener = ["(", "[", "{"]

        for i in s:
            # pdb.set_trace()
            if len(queue) == 0:
                if i in opener:
                    queue.append(i)
                else:
                    return False
            else:
                to_close = queue.pop()
                if closes[to_close] == i:
                    pass
                else:
                    if i not in opener:
                        return False
                    queue.append(to_close)
                    queue.append(i)

        return len(queue) == 0
