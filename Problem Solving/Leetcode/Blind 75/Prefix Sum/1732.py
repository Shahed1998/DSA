class Solution:
    def largestAltitude(self, gain):

        max_gain = 0
        curr_alt = 0

        for g in gain:

            curr_alt += g

            max_gain = max(max_gain, curr_alt)

        return max_gain



s = Solution()
s.largestAltitude([-5,1,5,0,-7])
s.largestAltitude(gain = [-4,-3,-2,-1,4,3,2])

        