from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # --------------------------------------------------------------------
        # Optimal Solution
        # --------------------------------------------------------------------
        if head is None or head.next is None:
            return None

        slow = head
        fast = head.next.next  # fast starts 2 steps ahead

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # slow is now the node just BEFORE the middle
        slow.next = slow.next.next

        return head

        # --------------------------------------------------------------------
        # My intuition
        # --------------------------------------------------------------------
        # if head is None or head.next is None:
        #     return None

        # length = 0
        # tmp = head

        # while tmp != None:
        #     tmp = tmp.next
        #     length += 1

        # index_to_be_deleted = length // 2

        # prev = head

        # for i in range(index_to_be_deleted-1):
        #     prev = prev.next

        # if prev is not None:
        #     prev.next = prev.next.next

        # return head

        
        


