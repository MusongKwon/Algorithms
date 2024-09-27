# Musong Kwon
# April 9, 2024
# Knapsack Problem

# items of weights 10, 20, 30 lbs with values $60, $100, $120; weight capacity is 50 lbs
v = [60, 100, 120]
w = [10, 20, 30]
W = 50
n = len(v)
q = []
for i in range(n):
    q.append(v[i] / w[i])

# sort lists for the greedy strategy
q.sort(reverse=True)
w_sorted = []
w_1 = {w[i]: q[i] for i in range(len(q))}
w_lst = {k: v for k, v in sorted(w_1.items(), reverse = True, key=lambda item: item[1])}
for i in w_lst.keys():
    w_sorted.append(i)

# dynamic programming
def zero_one_knapsack(n, val, weight, W):
    v = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                v[i][w] = 0
            elif weight[i-1] <= w:
                v[i][w] = max(val[i-1] + v[i-1][w-weight[i-1]], v[i-1][w])
            else:
                v[i][w] = v[i-1][w]
    return v[n][W]

# greedy strategy
def fractional_knapsack(n, q, w, W):
    load = 0
    value = 0
    i = 0
    while (load < W and i <= n):
        if w[i] <= (W - load):
            load += w[i]
            value += w[i] * q[i]
        else:
            value += (W - load) * q[i]
            load += (W - load)
        i += 1
    return value

print("max value of 0/1 knapsack using dynamic programming: $", zero_one_knapsack(n,v,w,W))
print("max vlaue of fractional knapsack using greedy strategy: $", fractional_knapsack(n, q, w_sorted, W))

