class Solution {
public:
    int minJumps(vector<int>& arr) {
        int N = arr.size();
        unordered_map<int, vector<int>> graph;
        unordered_set<int> visited;
        queue<int> Q;
        int level = 0;
        
        visited.insert(0);
        Q.push(0);
        
        for(int i = 0; i < N; i++){
            graph[arr[i]].push_back(i);
        }
        
        while(!Q.empty()){
            for(int size = Q.size(); size > 0; size--){
                int curr = Q.front(); Q.pop();
                
                if(curr == N - 1)
                    return level;
                
                vector<int>& next = graph[arr[curr]];
                next.push_back(curr + 1);
                next.push_back(curr - 1);
                
                for(int neigh : next){
                    if(0 <= neigh && neigh < N && visited.find(neigh) == visited.end() ){
                        visited.insert(neigh);
                        Q.push(neigh);
                    }
                }
                next.clear();
            }
            
            level++;
        }
        
        return level;
        
        
    }
};