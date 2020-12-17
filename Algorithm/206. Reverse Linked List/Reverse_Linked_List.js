/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let prevNode = null; // create a pointer before head
    
    while (head != null){
      let nextNode = head.next;
          head.next = prevNode;
          prevNode = head;
          head = nextNode;
    }
    // now the head is null, so return prevNode
    return prevNode;
}

// Link: https://leetcode.com/problems/reverse-linked-list/
