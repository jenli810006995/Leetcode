* Time: Aug 17 2020

Shuffle a set of numbers without duplicates.

Example:

```
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

```
* Logic: According to Larry on the Youtube, this was Fisher-Yales algorithms.

* Solution:
```
class Solution:
    def __init__(self, nums:List[int]):
        self.original = nums[:]
    def reset(self)-> List[int]:
        '''
        reset the array and configure to its original
        '''
        return self.original
    def shuffle(self)-> List[int]:
        '''
        return a random shuffing of the array
        '''
        results= self.original[:]
        random.shuffle(results)
        return results
```
* [Link](https://leetcode.com/problems/shuffle-an-array/)



