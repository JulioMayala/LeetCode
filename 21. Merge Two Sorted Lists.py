#Definition for singly-linked list.
class ListNode(object):
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        begin=my_list=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                my_list.next=list1
                list1=list1.next
            else:
                my_list.next=list2
                list2=list2.next
            my_list=my_list.next
        my_list.next=list1 or list2
        return begin.next