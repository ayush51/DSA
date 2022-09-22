class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr! = None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
         return
