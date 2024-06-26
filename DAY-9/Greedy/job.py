# profit = [20, 40, 10, 30, 50]
# deadline_lst = [2, 1, 2, 3, 1]
# deadline = max(deadline_lst)
#
# job_dict = {}
# for i in range(len(profit)):
#     if deadline_lst[i] not in job_dict:

# # Using recursive approach
# def cal_max(p, w, c, n):
#     if n == 0 or c == 0:
#         return 0
#     if w[n - 1] > c:
#         return cal_max(p, w, c, n - 1)
#     else:
#         return max(p[n - 1] + cal_max(p, w, c - w[n - 1], n - 1), cal_max(p, w, c, n - 1))
#
#
# p = [5, 10, 15, 7, 8, 9, 4]
# w = [1, 3, 5, 4, 1, 3, 2]
# c = 15
# n = len(p)
# print(cal_max(p, w, c, n))

# using memoisation:


# def calc_max(p, w, c, n):
#     if n == 0 or c == 0:
#         return 0
#     if DP[n][c] != -1:
#         return DP[n][c]
#     if w[n-1] <= c:
#         DP[n][c] = max(p[n - 1] + calc_max(p, w, c - w[n - 1], n - 1), calc_max(p, w, c, n - 1))
#         return DP[n][c]
#     else:
#         DP[n][c] = calc_max(p,w,c,n-1)
#         return DP[n][c]
#
# p = [5, 10, 15, 7, 8, 9, 4]
# w = [1, 3, 5, 4, 1, 3, 2]
# c = 15
# n = len(p)
# DP = [[-1 for i in range(c + 1)] for j in range(n + 1)]
# print(calc_max(p,w,c,n))

p = [5, 10, 15, 7, 8, 9, 4]
w = [1, 3, 5, 4, 1, 3, 2]
c = 15
n = len(p)
DP = [[0 for i in range(c + 1)] for j in range(n + 1)]

for i in range(n+1):
    for c in range(n+1):
        DP[i][c] = max(DP[i-1][c], p[i-1]+DP[i-1][c-w[i-1]])

print(DP)
print(51)
