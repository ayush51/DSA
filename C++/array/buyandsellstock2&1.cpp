class Solution {
public:
    int maxProfit(vector<int>& prices) {
      int profit = 0;
    for (int i =1; i<prices.size(); i++){
        if(prices[i]>prices[i-1]){
            profit+=(prices[i]-prices[i-1]);
        }
    }
        return profit;
    }
};

/////////////////////////

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int minsofar=prices[0];
        
        for(int i=0; i<prices.size();i++){
            minsofar=min(prices[i],minsofar);
            int profit = prices[i]-minsofar;
            maxProfit = max(profit, maxProfit);
        }
        return maxProfit;
    }
};

//////////////////////////////
