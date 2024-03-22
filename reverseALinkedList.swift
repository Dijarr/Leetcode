/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {
        var prev = ListNode?(nil)
        var head = head
        while head != nil {
            var next = head?.next
            head?.next = prev

            prev = head
            head = next

        }
        return prev
    }

}

// time and space complexity = O(n),O(1)
