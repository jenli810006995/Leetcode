var rotate = function(nums, k){
    const n = nums.length;
    k %= n;
    reverse(nums, 0, n - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, n - 1);

}

function reverse(arr, start, end){
    while (start < end){
    [arr[start], arr[end]] = [arr[end], arr[start]];
    start ++;
    end --;
    }
}


## Link: https://leetcode.com/problems/rotate-array/
## Reference: https://www.youtube.com/watch?v=8kyZPizZzWc
