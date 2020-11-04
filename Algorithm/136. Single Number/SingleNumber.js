var singleNumber = function(nums){
// create a hashset

    const set1 = new Set();
    
    for (i = 0; i < nums.length; i ++){
        if (set1.has(nums[i])){
            // remove it from the set
            set1.delete(nums[i]);
        else
            set1.add(nums[i]);
        }
    }

    for (let item of set1)
        return item;

};



// Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

// Reference: https://youtu.be/CvnnCZQY2A0

// Reference: https://youtu.be/_4r2ex3GKQ8

