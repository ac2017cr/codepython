import time

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

def sortarray(arr, out=[]):
    chunk = 2
    if (len(arr) <= 1): return arr
    if (arr == None): return []
    temp = []

    for i in range(0, len(arr), chunk):
        temp = arr[i:i+chunk]
        if len(temp) > 1:
            if temp[0] > temp[1]:
                temp[0], temp[1] = temp[1], temp[0]
        out = merge(temp, out)

    return out

start_time = time.time()
arr = [9, 8, 2, 6, 5, 4, 3, 7, 1]
print(sortarray(arr))
print("--- %s seconds ---" % (time.time() - start_time))