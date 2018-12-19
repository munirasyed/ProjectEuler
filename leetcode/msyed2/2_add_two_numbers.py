# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        root=ListNode(0)
        prev=root
        curr=root
        while l1 or l2 or carry:
            if carry:
                curr.val+=carry
            carry=0
            if l1:
                curr.val+=l1.val
                
                l1=l1.next
                
            if l2:
                curr.val+=l2.val
                l2=l2.next
            #print(curr.val)
            if curr.val>9:
                curr.val=curr.val%10
                carry=1
            if l1 or l2 or carry:
                prev.next=curr
                prev=curr
                curr.next = ListNode(0)
                curr=curr.next
        return root    
