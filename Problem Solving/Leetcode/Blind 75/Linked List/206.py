class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev