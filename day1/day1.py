"""
1. Import the file - input
2. Create two lists out of the file
3. Sort the two list in a ascending manner
4. Then sub a[1] from b[1] and then find out the difference
5. Add the difference and find total distance

"""
a = []
b = []
import os
from collections import Counter

with open('input', 'r') as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split())
        a.append(x)
        b.append(y)
a.sort()
b.sort()
n = len(a)

'''
multiply a[i] with the numbr of times it appears in right list.
- how many times does a[i] appear in b
Then add all the values in a
'''

freq = Counter(b)
print(sum(a[i] * freq[a[i]] for i in range(n)))
