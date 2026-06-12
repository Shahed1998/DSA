from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()
        self.ptr = 0
    

    def ping(self, t: int) -> int:

        self.requests.append(t)
        lower_bound = t - 3000

        # this is an intuitive 2 pointer solution, the only problem is memory space complexity will be high on large data
        # becase no data gets removed
        # while self.requests[self.ptr] < lower_bound:
        #     self.ptr += 1
        # return (len(self.requests)-self.ptr)

        # better approach, use linked list
        # Physically remove elements that fall outside the 3000ms window
        while self.requests[0] < lower_bound:
            self.requests.popleft()


        print(len(self.requests))

        

        
            





        
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
recentCounter = RecentCounter()
recentCounter.ping(1);     #// requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   #// requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  #// requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  #// requests = [1, 100, 3001, 3002], range is [2,3002], return 3