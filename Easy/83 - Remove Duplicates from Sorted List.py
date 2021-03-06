#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        curr = head
        
        while curr and curr.next:
            
            if curr.val == curr.next.val:
                curr.next=curr.next.next
            
            if curr.next is not None:
                if curr.val!=curr.next.val:
                    curr = curr.next
            else:
                break

        return head
