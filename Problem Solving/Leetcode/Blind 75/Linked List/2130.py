
# ----------------------------------------------------------------------------------------------
# Unoptimal: My generated solution for the problem is as follows:
# ----------------------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
        
#         list_len = 0

#         node = head

#         while node:
#             node = node.next
#             list_len += 1

#         hashMap = {}
#         maxSum = 0

#         find_twin_upto = (list_len/2)-1

#         curr_node = head

#         for i in range(list_len):
            
#             if 0 <= i <= find_twin_upto:
                
#                 twin = list_len - 1 - i

#                 hashMap[twin] = curr_node.val  

#             if i in hashMap:
#                 maxSum = max(maxSum, curr_node.val + hashMap[i])

#             curr_node = curr_node.next

#         return maxSum
        


# ----------------------------------------------------------------------------------------------
# Optimal Solution
# ----------------------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head) -> int:

        # ---------------------------------------------------
        # Step 1: Find the middle of the linked list.
        #
        # Slow moves 1 step.
        # Fast moves 2 steps.
        #
        # Since the list length is guaranteed to be even,
        # slow will stop at the FIRST node of the second half.
        #
        # Example:
        # 5 -> 4 -> 2 -> 1
        #           ^
        #         slow
        # ---------------------------------------------------
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # ---------------------------------------------------
        # Step 2: Reverse the second half.
        #
        # Before:
        # 5 -> 4 -> 2 -> 1
        #
        # Second half:
        # 2 -> 1
        #
        # After reversing:
        # 1 -> 2
        #
        # Now the twin nodes are aligned:
        #
        # First half : 5 -> 4
        # Second half: 1 -> 2
        #
        # So we can simply walk both lists together.
        # ---------------------------------------------------
        prev = None
        curr = slow

        while curr:
            nxt = curr.next      # Save next node
            curr.next = prev     # Reverse current pointer
            prev = curr          # Move prev forward
            curr = nxt           # Move current forward

        # Head of reversed second half
        second = prev

        # Head of first half
        first = head

        # ---------------------------------------------------
        # Step 3: Traverse both halves simultaneously.
        #
        # Twin pairs are now:
        #
        # first   second
        #   5   +   1
        #   4   +   2
        #
        # Compute the maximum twin sum.
        # ---------------------------------------------------
        max_sum = 0

        while second:
            max_sum = max(max_sum, first.val + second.val)

            first = first.next
            second = second.next

        return max_sum








        