// 31-bit signed integer: 2147483647, -2147483648

class Solution{
    public int myAtoi(String str){
    
    int i = 0;
    int sign = 1;
    int result = 0;
    
    // if length is 0 return 0
    
    if (str.length() == 0) return 0;
    
    // Discard white spaces
    while (i < str.length() && str.charAt(i) == ' ')
        i ++;
     
    // check if optional sign exists
    if (i < str.length() && (str.charAt(i) == '+' || str.charAt(i) == '-'))
        sign = (str.charAt(i ++) == 1) ? -1 : 1;
    
    // build result and check for overflow/underflow
    
    while (i < str.length() && str.charAt(i) >= '0' && str.charAt(i) <= '9'){
        // check overflow/ underflow
        if (result >  Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10 && str.charAt(i) - '0' > Integer.MAX_VALUE % 10))
            return (sign == 1)? Integer.MAX_VALUE: Integer.MIN_VALUE;
            result = result * 10 + str.charAt(i ++) - '0';
    }
    return result * sign;
    }
}


// Time: O(n); Space: O(1)

