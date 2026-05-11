class Solution:


    # efficient approach
    def canPlaceFlowers(self, flowerbed, n):

        for i in range(len(flowerbed)):

            if flowerbed[i] == 1: continue

            lptr = (i == 0 or flowerbed[i-1] == 0)
            rptr = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)

            if lptr and rptr:
                flowerbed[i] = 1
                n -= 1
            
            if n <= 0:
                return True
            
        return False

    
    # My approach
    # def canPlaceFlowers(self, flowerbed, n):

    #     for mptr in range(len(flowerbed)):
    #         rptr = mptr+1
    #         lptr = mptr-1

    #         if lptr < 0 and rptr >= len(flowerbed) and flowerbed[mptr] == 0:
    #             flowerbed[mptr] = 2
    #             n-=1

    #         if lptr < 0 and rptr < len(flowerbed) and flowerbed[mptr] == 0 and flowerbed[rptr] == 0:
    #             flowerbed[mptr] = 2
    #             n-=1

    #         if lptr >= 0 and rptr >= len(flowerbed) and flowerbed[mptr] == 0 and flowerbed[lptr] == 0:
    #             flowerbed[mptr] = 2
    #             n-=1

    #         if lptr >= 0 and rptr < len(flowerbed) and flowerbed[mptr] == 0 and flowerbed[lptr] == 0 and flowerbed[rptr] == 0:
    #             flowerbed[mptr] = 2
    #             n-=1

    #     print(flowerbed)
    #     return False if n >= 1 else True


s = Solution()
# print(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
# print(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
# print(s.canPlaceFlowers([0,1,0], 1))
# print(s.canPlaceFlowers([0,1,0,1,0,1,0,0], 1))
print(s.canPlaceFlowers([0,0,1,0,1], 1))