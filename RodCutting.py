# Musong Kwon
# March 25, 2024
# Rod Cutting Problem

import time

# cut rod
def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q

# memoized cut
def memoized_cut_rod(p, n):
    r = []
    for i in range(n + 1):
        r.append(i)
    for i in range(n + 1):
        r[i] = float('-inf')
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q

# extended bottom up cut
def extened_bottom_up_cut_rod(p, n):
    r = []
    s = []
    for i in range(n + 1):
        r.append(i)
    for i in range(n + 1):
        s.append(i)
    r[0] = 0
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i] + r[j - i] :
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s

def print_cut_rod_solution(p, n):
    r, s = extened_bottom_up_cut_rod(p, n)
    while n > 0:
        print (s[n])
        n = n - s[n]

# price
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

#1
print('#1')
n = 1
start = time.time()
cut_rod(p, n)
end = time.time()
print('cut rod:', cut_rod(p, n))
print('cut rod running time:', (end-start) * 10**3)

start_time = time.time()
memoized_cut_rod(p, n)
end = time.time()
print('memoized cut:', memoized_cut_rod(p, n))
print('memoized cut running time:', (end-start) * 10**3)

start_time = time.time()
extened_bottom_up_cut_rod(p, n)
end = time.time()
print('extended bottom up cut:', extened_bottom_up_cut_rod(p, n))
print('extended bottom up cut running time:', (end-start) * 10**3)

#2
print('#2')
n = 2
start = time.time()
cut_rod(p, n)
end = time.time()
print('cut rod:', cut_rod(p, n))
print('cut rod running time:', (end-start) * 10**3)

start_time = time.time()
memoized_cut_rod(p, n)
end = time.time()
print('memoized cut:', memoized_cut_rod(p, n))
print('memoized cut running time:', (end-start) * 10**3)

start_time = time.time()
extened_bottom_up_cut_rod(p, n)
end = time.time()
print('extended bottom up cut:', extened_bottom_up_cut_rod(p, n))
print('extended bottom up cut running time:', (end-start) * 10**3)

#3
print('#3')
n = 3
start = time.time()
cut_rod(p, n)
end = time.time()
print('cut rod:', cut_rod(p, n))
print('cut rod running time:', (end-start) * 10**3)

start_time = time.time()
memoized_cut_rod(p, n)
end = time.time()
print('memoized cut:', memoized_cut_rod(p, n))
print('memoized cut running time:', (end-start) * 10**3)

start_time = time.time()
extened_bottom_up_cut_rod(p, n)
end = time.time()
print('extended bottom up cut:', extened_bottom_up_cut_rod(p, n))
print('extended bottom up cut running time:', (end-start) * 10**3)

#4
print('#4')
n = 4
start = time.time()
cut_rod(p, n)
end = time.time()
print('cut rod:', cut_rod(p, n))
print('cut rod running time:', (end-start) * 10**3)

start_time = time.time()
memoized_cut_rod(p, n)
end = time.time()
print('memoized cut:', memoized_cut_rod(p, n))
print('memoized cut running time:', (end-start) * 10**3)

start_time = time.time()
extened_bottom_up_cut_rod(p, n)
end = time.time()
print('extended bottom up cut:', extened_bottom_up_cut_rod(p, n))
print('extended bottom up cut running time:', (end-start) * 10**3)

#5
print('#5')
n = 5
start = time.time()
cut_rod(p, n)
end = time.time()
print('cut rod:', cut_rod(p, n))
print('cut rod running time:', (end-start) * 10**3)

start_time = time.time()
memoized_cut_rod(p, n)
end = time.time()
print('memoized cut:', memoized_cut_rod(p, n))
print('memoized cut running time:', (end-start) * 10**3)

start_time = time.time()
extened_bottom_up_cut_rod(p, n)
end = time.time()
print('extended bottom up cut:', extened_bottom_up_cut_rod(p, n))
print('extended bottom up cut running time:', (end-start) * 10**3)