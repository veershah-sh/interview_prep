#!/bin/python3

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    result = 0
    ar.sort()
    i = 0
    while i < (n-1):
        if(ar[i] == ar[i + 1]):
            result += 1
            i = i + 2
        else:
            i += 1
    return result


if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)