class Solution{
    public String longestCommonPrefix(String[] strs){
    String longestCommonPrefix = "";
    if (strs == null || strs.length == 0){
        return longestCommonPrefix;
    }
    
    int index = 0;
    for (char c: strs[0].toCharArray()){
        for (int i = 1; i < strs.length; i ++){
            if (index >= strs[i].length() || c != strs[i].charAt(index)){
                return longestCommonPrefix;
                }
            }
        longestCommonPrefix += c;
        index ++;  
        }
     return longestCommonPrefix;
   }
}

/* Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/  */
/* Reference: https://youtu.be/1YQmI7F9dJ0  */

