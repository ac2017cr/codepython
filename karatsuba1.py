import math, time
#7006652 (OK for 5678 and 1234)

def zeroPad(numberString, zeros, left = True):
    """Return the string with zeros added to the left or right."""
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString

def multiply(num1, num2):
    str1 = str(num1)
    str2 = str(num2)

    if len(str1) == 1 and len(str2) == 1: 
        return  num1 * num2
    if len(str1) < len(str2):
        str1 = zeroPad(str1, len(str2) - len(str1))
    elif len(str2) < len(str1):
        str2 = zeroPad(str2, len(str1) - len(str2))
    if (len(str1) % 2 != 0):
        str1 = zeroPad(str1, 1)
        str2 = zeroPad(str2, 1)

    n = len(str1)
    mid = int(n/2)
    a = int(str1[0:mid])
    b = int(str1[mid:])
    c = int(str2[0:mid])
    d = int(str2[mid:])
    p = a + b
    q = c + d
    ac = multiply(a, c)
    bd = multiply(b, d)
    pq = multiply(p, q)
    adbc = pq - ac - bd

    ac = int(zeroPad(str(ac), n, False))
    adbc = int(zeroPad(str(adbc), mid, False))

    #return 10**n*ac+10**mid*adbc+bd
    return ac + adbc + bd

#
#    star: 10**n*a*c + 10**mid*(a*d + b*c) + b*d
#
start_time = time.time()
#num1 = 5678
#num2 = 1234
num1 = 5678251
num2 = 34339
print(multiply(num1, num2))
print("--- %s seconds ---" % (time.time() - start_time))