* Time: Aug 26 2020

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

Example 2:
```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

Example 3:
```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

 

Follow-up:
Can you solve it without using extra space?

* Logic: Imagine two persons running in the track field. One is fast and the other is slow

* Solution:

```
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 
 public class Solution{
     public ListNode detectCycle(ListNode head){
         
         if (head == null) return null;
         
         /* specify parameters */
         
         ListNode slow = head, fast = head;
         
         try{
           do {
               fast = fast.next;
               fast = fast.next;
               slow = slow.next;
           } while (fast != null && slow != fast);
           }catch (Exception e){}
         
         if (slow == null || fast == null || slow != fast)
             return null;
             
         slow = head;
         
         while (slow != fast){
             slow = slow.next;
             fast = fast.next;
         }return slow;
     }
 }

```

* [Link](https://leetcode.com/problems/linked-list-cycle-ii/)

* [Credit](https://gist.github.com/ericpony/45c14deda5dd85f5e981)
