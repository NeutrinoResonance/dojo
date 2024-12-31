class Solution(object):
    def addTwoNumbers(self, one, two):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        assert all([isinstance(f, ListNode) for f in [one, two]])

        output = None
        output_head = None

        current_one = one
        current_two = two
        carry = 0

        while current_one != None or current_two != None:
            current = (current_one.val if current_one != None else 0) + \
                      (current_two.val if current_two != None else 0) + \
                      carry

            current_add = None
            if current >= 10:
                carry = 1
                current_add = ListNode(current - 10)
            else:
                carry = 0
                current_add = ListNode(current)

            if output == None:
                output = current_add
                output_head = current_add
            else:
                output_head.next = current_add
                output_head = current_add

            if current_one != None:
                current_one = current_one.next

            if current_two != None:
                current_two = current_two.next

        if carry != 0:
            output_head.next = ListNode(carry)
            carry = 0

        return output
