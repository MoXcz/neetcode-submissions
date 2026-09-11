class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur is not None:
            sub = cur.next
            cur.next = prev

            prev = cur
            cur = sub

        return prev