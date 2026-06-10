class RecentCounter:

    def __init__(self):
        self.requestsBefore3000 = 0
        self.crossed3000 = 0
        

    def ping(self, t: int) -> int:

        if t <= 3000:
            self.requestsBefore3000 += 1

        elif self.crossed3000 == 0:
            self.requestsBefore3000 += 1
            self.crossed3000 += 1

        return self.requestsBefore3000
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
recentCounter = RecentCounter()
recentCounter.ping(1);     #// requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   #// requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  #// requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  #// requests = [1, 100, 3001, 3002], range is [2,3002], return 3