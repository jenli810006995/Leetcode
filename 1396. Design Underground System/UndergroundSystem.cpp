'''
referred to https://www.acwing.com/solution/LeetCode/content/10643/
'''
class UndergroundSystem {
public:
    unordered_map<int , pair<string, int>> in;
    unordered_map<string, unordered_map<string , pair<double, int>>> ans;
    
    UndergroundSystem (){
    }
    
    void checkIn(int id, string stationName, int t){
        in[id] = make_pair(stationName, t);
    }
    
    void checkOut(int id, string stationName, int t){
        ans[in[id].first][stationName].first += t - in[id].second;
        ans[in[id].first][stationName].second++;
    }
    
    double getAverageTime(string startStation, string endStation) {
        return ans[startStation][endStation].first/ans[startStation][endStation].second;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */
 
 # Time Complexity: O(1)
 # Space Complexity: O(n)
 
 
