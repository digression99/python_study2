# def binarySearch(dat, old, new, tgt):
#     cnt = 0
#     for d in dat:
#         cnt += (d // new)
#
#     if old == new:
#         return cnt
#
#     if cnt > tgt: # decreased from before? nobody knows.
#         if binarySearch(dat, old, old, tgt) == tgt:
#             return old
#         else:
#             return binarySearch(dat, new, new + 1, tgt)
#     elif cnt < tgt: # increased from before.
#         # return binarySearch(dat, old, old, tgt)
#         if binarySearch(dat, old, old, tgt) == tgt:
#             return old
#         else:
#             return binarySearch(dat, new, new - 1, tgt)
#     elif cnt == tgt:
#         if old < new:
#             return binarySearch(dat, new, new + 1, tgt)
#         elif old > new:
#             return new
#
# rep = input()
# pieces = rep.split()
# k = int(pieces[0])
# n = int(pieces[1])
# dat = []
#
# for i in range(0, k):
#     dat.append(int(input()))
#
# m = sum(dat) // n
# ans = binarySearch(dat, m, m + 1, n)
# print(ans)
# # there is
