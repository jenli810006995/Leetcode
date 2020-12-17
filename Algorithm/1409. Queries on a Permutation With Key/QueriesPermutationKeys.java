'''
referred to https://www.cnblogs.com/lz87/p/12695500.html
'''
class Solution {
    public int[] processQueries(int[] queries, int m) {
        int[] v = new int[m];
        for (int i = 0 ; i < m ; i++ ){
            v[i] = i+1;
        }
        
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++){
            int j = 0;
            for (; j < m; j++){
                if (queries[i] == v[j]){
                    break;
                }
            }
            ans[i] = j;
            int temp = v[0];
            v[0] = v[j];
            v[j] = temp;
            reverse( v, 1, j-1);
            reverse(v, 1 , j);
        }
        return ans;
    }
    private void reverse(int[] v, int i, int j){
        while (i < j){
            int temp = v[i];
            v[i] = v[j];
            v[j] = temp;
            i ++;
            j--;
        }
    }
}

