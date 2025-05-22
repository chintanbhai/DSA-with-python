# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head = list1(0,)
        tempList = ListNode()
        point = tempList

        while list1 and list2:
            
            if list1.val < list2.val:
                print("---->",list1.val)
                point.next = list1
                list1 = list1.next
            else:
                print("---->",list2.val)
                point.next = list2
                list2 = list2.next
            point=point.next
        
        point.next = list1 if list1 else list2
        
        return tempList.next

            

s1 = ListNode(1)
s2 = ListNode(2)
s3 = ListNode(4)
s1.next = s2
s2.next = s3

s4 = ListNode(1)
s5 = ListNode(3)
s6 = ListNode(4)
s4.next = s5
s5.next = s6
s = Solution()
result = s.mergeTwoLists(s1, s4)
while result:
    print(result.val)
    result = result.next