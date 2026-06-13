from collections import deque

class Solution:
    def predictPartyVictory(self, senate):

        D_party = deque()
        R_party = deque()
        n = len(senate)

        for i,s in enumerate(senate):

            if s == "R":
                R_party.append(i)
            else:
                D_party.append(i)

        while D_party and R_party:

            d_index = D_party.popleft()
            r_index = R_party.popleft()


            if r_index < d_index:
                R_party.append(r_index + n)
            else:
                D_party.append(d_index + n)

        return "Dire" if D_party else "Radiant"





s = Solution()
# print(s.predictPartyVictory(senate = "DDRRR"))
print(s.predictPartyVictory(senate = "RD"))
# s.predictPartyVictory(senate = "RDD")
