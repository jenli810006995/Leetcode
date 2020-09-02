Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

```
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
```

* Solution in Java:
```
class Solution {
    private Random rand;
    private int[] nums;
    private int k = 1;
    
    public Solution(int[] nums) {
        rand = new Random();
        this.nums = nums;
    }
    
    
    public int pick(int target){
       int result = -1;
       int count = 0;
       for (int i = 0; i < nums.length; i++){
           if (nums[i] == target){
               count++;
               if (rand.nextInt(count) < k){
                   result = i;
               }
               
           }
       }
           
    return result;
    }        
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */

```

* [Link](https://leetcode.com/problems/random-pick-index/)
* [Reference](https://aaronice.gitbook.io/lintcode/random/random-pick-index)

