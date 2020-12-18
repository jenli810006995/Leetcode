/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    // create two pointers
    let fastPointer = head;
    let slowPointer = head;
    
    // while loop for the fastpointer is not null
    while (fastPointer !== null && fastPointer.next !== null){
        fastPointer = fastPointer.next.next;
        slowPointer = slowPointer.next;
        if (fastPointer == slowPointer){
          return true;
        }
    }
    return false;
};
// Link: https://leetcode.com/problems/linked-list-cycle/
