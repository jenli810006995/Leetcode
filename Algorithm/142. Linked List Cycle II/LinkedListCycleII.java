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
         
         /*specify parameters*/
         
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
             fast = fast.next;
             slow = slow.next;
         }return slow;
     }
 }
