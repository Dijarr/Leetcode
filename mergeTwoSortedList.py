class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = dummy = ListNode()
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                dummy.next = list1
                # it's dummy.next = list1 cos it's the node we're rearranging and not the value
                list1 = list1.next
            
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next
        dummy.next = list1 or list2 
        return result.next