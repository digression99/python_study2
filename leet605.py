class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        ln = len(flowerbed)
        if ln == 1 and flowerbed[0] == 1:
            return False
        elif ln == 1 and flowerbed[0] == 0:
            return True

        for i in range(ln):
            if n <= 0:
                return True
            if (i == 0 and i == ln - 1) and flowerbed[i] == 0:
                n -= 1
                flowerbed[i] = 1
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
            if i == ln - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                n -= 1
                flowerbed[i] = 1
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
        else:
            if n == 0:
                return True
        return False


fb = [1, 0, 0, 0, 0, 1]
fb2 = [1,0,0,0,1,0,0]
n = 2
print(Solution().canPlaceFlowers(fb2, n))