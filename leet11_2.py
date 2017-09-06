class Solution(object):

    def __init__(self):
        self.matrix = []

    def maxArea(self, height):
        self.matrix = [-1] * len(height)
        maxspace = 0
        left = 0
        right = 0
        ans = 0

        for i in range(len(height)):
            if self.matrix[i] == -1:
                maxspace = 0
                for j in range(len(height)):
                    if i == j: continue
                    short = height[i] if height[i] < height[j] else height[j]
                    s = abs(j - i) * short
                    if maxspace < s:
                        if ans < s:
                            ans = s
                        maxspace = s
                        left = j if j < i else i
                        right = i if j < i else j

                self.matrix[left] = right
                self.matrix[right] = left

        return ans




            # for j in range(len(height)):
            #     if self.matrix[i] == -1:
            #         maxspace = 0






    # def dp(self, start, l):
    #     #if self.matrix[l]
    #
    # def maxArea(self, height):
    #     self.matrix = [[-1] * len(height) for i in range(len(height))]
    #
    #     maxspace = 0
    #     left = 0
    #     right = 0
    #
    #     for i in range(len(height)):
    #         for j in range(i + 1, len(height)):
    #             short = height[i] if height[i] < height[j] else height[j]
    #             s = (j - i) * short
    #
    #             if s > maxspace:
    #                 maxspace = s
    #                 left = i
    #                 right = j
    #     return maxspace

        """
        :type height: List[int]
        :rtype: int
        """
