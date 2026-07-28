class Solution:
    def oddEvenList(self, head):

        if head is None or head.next is None or head.next.next is None: return head

        odd = head
        even = head.next
        tmp_even = even

        while odd.next is not None and even.next is not None:

            odd.next = even.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = tmp_even

        return head