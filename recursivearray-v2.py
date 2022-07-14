import math, time

def merge(a, b):
    m = []
    i = 0
    j = 0
    while(True):
        if len(a) in [0, i]:
            m += b[j:]
            break
        elif len(b) in [0, j]:
            m += a[i:]
            break
        elif a[i] < b[j]:
            m.append(a[i])
            i += 1
        else:
            m.append(b[j]) 
            j += 1
    print(m)
    return m

def sortarray(arr):
    n = len(arr)
    if (n < 2): return arr
    mid = math.floor(n/2)
    l = arr[0:mid]
    r = arr[mid:]
    l = sortarray(l)
    r = sortarray(r)
    return merge(l, r)

start_time = time.time()
arr = [11, 1, 9, 8, 2, 6, 10, 5, 4, 3, 7]
print(sortarray(arr))
print("--- %s seconds ---" % (time.time() - start_time))