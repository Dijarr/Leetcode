class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = dummy = ListNode()
        carry = 0
        while l1 or l2:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
                
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
                
            result = v1 + v2 + carry
            carry = result // 10
            remainder = result % 10
            dummy.next = ListNode(remainder)
            dummy = dummy.next
            
        
        if carry:
            dummy.next = ListNode(carry)

        return answer.next
