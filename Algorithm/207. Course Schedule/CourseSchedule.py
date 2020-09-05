class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = [[] for x in range(numCourses)]
        ind = [0 for x in range(numCourses)]
    
        for p in prerequisites:
            if p[0] not in map[p[1]]:
                ind[p[0]] += 1
                map[p[1]].append(p[0])
            
        st = []
        for i in range(numCourses):
            if ind[i] == 0:
                st.append(i)
            
        count = 0
        while st:
            tmp = st[0]
            st.pop(0)
            count +=1
            for i in map[tmp]:
                ind[i]-=1
                if ind[i] == 0:
                    st.append(i)
                
        if count < numCourses:
            return False
        else:
            return True
        
## Link: https://leetcode.com/problems/course-schedule/
## Reference: http://yucoding.blogspot.com/2015/06/leetcode-question-course-schedule.html
