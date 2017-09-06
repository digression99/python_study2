class Solution(object):
    def distributeCandies(self, candies):
        if len(candies) <= 2:
            return 1

        candies.sort()
        half = len(candies) // 2
        j = half
        cnt = 0
        for i in range(len(candies) - half - 1):
            if candies[j] == candies[j + 1] and candies[i] != candies[j]:
                candies[i], candies[j] = candies[j], candies[i]
                cnt += 1
            elif candies[j] != candies[j + 1]:
                cnt += 1
            j += 1
        return cnt + 1

    def distributeCandies2(self, candies):
        i, j = 0, len(candies) // 2
        cnt = 0

        while i < len(candies) // 2:
            while i < len(candies) // 2 and candies[i] == candies[i + 1]:
                i += 1
            while j < len(candies) and candies[j] == candies[j + 1]:
                j += 1

            if candies[i] != candies[j]:
                candies[i], candies[j - 1] = candies[j - 1], candies[i]
                cnt += 1
            i += 1
        while j < len(candies) - 1:
            while j < len(candies) - 1 and candies[j + 1] == candies[j]:
                j += 1
            if j < len(candies) - 1 and candies[j + 1] != candies[j]:
                cnt += 1
            j += 1
        return cnt + 1
















        """
        :type candies: List[int]
        :rtype: int
        """

l = [1, 1, 2, 2, 3, 3]
l2 = [1, 1, 2, 3]
l3 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
print(Solution().distributeCandies2(l3))