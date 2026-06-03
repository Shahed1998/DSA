class Solution:
    def asteroidCollision(self, asteroids):

        stack = []

        for a in asteroids:

            alive = True

            while alive and stack and stack[-1] > 0 and a < 0:

                if abs(a) > stack[-1]:
                    stack.pop()

                elif abs(a) == stack[-1]:
                    stack.pop()
                    alive = False

                else:
                    alive = False

            if alive:
                stack.append(a)

        return stack
            


            






s = Solution()
# s.asteroidCollision(asteroids = [10,3,4,-5])
print(s.asteroidCollision(asteroids = [3,5,-6,2,-1,4]))

