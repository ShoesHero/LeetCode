
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        k = count - k % count
        if k == count:
            return head

        cur = head
        while k > 1:
            cur = cur.next
            k -= 1

        new_head = cur.next
        to_last = cur.next
        while to_last.next:
            to_last = to_last.next

        to_last.next = head
        cur.next = None
        return new_head