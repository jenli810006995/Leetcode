var removeNthFromEnd = function(head, n) {
  // create a dummy
  
  let dummy = new ListNode();
  length = 0;
  dummy.next = head;
 
  let first = new ListNode();
  first = head;
  // while loop
  while (first != null){
    length ++;
    first = first.next;
  }
 length -= n;
 first = dummy;
 while(length > 0){
   length --;
   first = first.next;
 }
 
 first.next = first.next.next;
 return dummy.next;
};

// Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
