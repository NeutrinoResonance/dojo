class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.forward = None
        self.back = None

        # used in the case of this node corresponding with a minimum
        self.min_forward = None
        self.min_back = None
        
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minimum = None
        self.head = None
        self.start = None

    def adjust_min(self, node, adjust_type="add"):
        if adjust_type == "add":
            if self.minimum == None:
                self.minimum = node
            else:
                if self.minimum.value > node.value:
                    self.minimum.min_forward = node
                    node.min_back = self.minimum
                    self.minimum = node
        elif adjust_type == "remove":
            # We assume that immediately after this operation,
            # node will be removed from the stack
            if self.minimum == None:
                pass
            else:
                if self.minimum == self.head:
                    if self.minimum.min_back != None:
                        self.minimum = self.minimum.min_back
                    else:
                        self.minimum = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        node = ListNode(x)
        if self.head != None:
            self.head.forward = node
            node.back = self.head
        self.adjust_min(node, "add")
        self.head = node
        
    def pop(self):
        """
        :rtype: void
        """
        if self.head != None:
            self.adjust_min(self.head, "remove")
            if self.head.back != None:
                self.head = self.head.back
            else:
                self.head = None
        else:
            pass

    def top(self):
        """
        :rtype: int
        """
        if self.head != None:
            return_value = self.head.value
            return return_value
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.minimum != None:
            return self.minimum.value
        else:
            return None
