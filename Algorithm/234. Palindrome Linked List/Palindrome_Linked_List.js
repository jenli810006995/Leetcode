var isPalindrome = function(head) {
    let fast = head;
    let slow = head;
    
    while (fast != null && fast.next != null){
        slow = slow.next;
        fast = fast.next.next;
    }
    
    fast = head;
    slow = reverse(slow)
    
    while (slow != null){ // which means it is not at the end (while not till the end)
      if (slow.val != fast.val){
        return false;
      }
      slow = slow.next;
      fast = fast.next;
    }
    return true;
 };

let reverse = function(head){
  let prevNode = null;
  
  while (head != null){
    let nextNode = head.next;
        head.next = prevNode;
        prevNode = head;
        head = nextNode;
  }
  return prevNode;
}

-- Link: https://leetcode.com/problems/palindrome-linked-list/
