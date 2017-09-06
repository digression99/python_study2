class Solution(object):
    def squareCheck(self, vert, hor):
        if vert * hor == hor ** 2:
            return True
        return False
    def move(self, points, idx, val):
        for i in range(4):
            points[i][idx] += val

    def validSquare(self, p1, p2, p3, p4):
        points = [p1, p2, p3, p4]
        for i in range(4):
            if points[i][0] < 0:
                self.move(points, 0, abs(points[i][0]))
            if points[i][1] < 0:
                self.move(points, 1, abs(points[i][1]))
        minx = 10000
        maxx = -10000
        miny = 10000
        maxy = -10000
        for i in range(4):
            if points[i][0] < minx:
                minx = points[i][0]
            if points[i][0] > maxx:
                maxx = points[i][0]
            if points[i][1] < miny:
                miny = points[i][1]
            if points[i][1] > maxy:
                maxy = points[i][1]

        dict = {}
        for i in range(4):
            dict.setdefault(points[i][0], 0)
            dict[points[i][0]] += 1
            dict.setdefault(points[i][1], 0)
            dict[points[i][1]] += 1
            if dict[points[i][0]] > 4 or dict[points[i][1]] > 4:
                return False

            if (points[i][0] != maxx and points[i][0] != minx) and \
                   (points[i][1] != miny and points[i][1] != maxy):
                return False



        return self.squareCheck(maxx - minx, maxy - miny)


        # for i in range(1, 4):
        #     if points[0][0] != points[i][0] and points[0][1] != points[i][1]:
        #         return self.squareCheck(abs(points[i][0] - points[0][0]), abs(points[i][1] - points[0][1]))
        # return False

p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]

p5 = [1134,-2539]
p6 = [492,-1255]
p7 = [-792,-1897]
p8 = [-150,-3181]

p9 = [1,0]
p10 = [-1,0]
p11 = [0,1]
p12 = [0,-1]

p13 = [0,0]
p14 = [1,1]
p15 = [1,0]
p16 = [0,1]

p17 = [1,1]
p18 = [5,3]
p19 = [3,5]
p20 = [7,7]

print(Solution().validSquare(p13, p14, p15, p16))
