# Definition for singly-linked list.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 != None and list2 == None:
            return list1
        elif list1 == None and list2 != None:
            return list2
        elif list1 == None and list2 == None:
            return None
        elif list1.val <= list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        