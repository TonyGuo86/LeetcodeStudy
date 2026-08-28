'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   8/27/2026 5:12 PM
*  @Project :   Leetcode
*  @FileName:   20260727.py
*  @Function:   tony add
**************************************
'''

import inspect
from collections import defaultdict

from cv2.datasets import index

'''
1208. 尽可能使字符串相等 1497
这个题目的
'''
def equalSubstring( s, t, maxCost):
    ans, left, cost = 0, 0, 0
    for right, c in enumerate(s):
        cost += abs(ord(s[right]) - ord(t[right]))
        if cost <= maxCost:
            ans = max(ans,right - left + 1)
            continue
        cost -= abs(ord(s[left]) - ord(t[left]))
        left += 1
    return ans

'''
904. 水果成篮 1516
这个题，你还是看了答案出来的，你好像椅一直在纠结一个循环是不是可以出来
'''
def totalFruit(fruits):
    try:
        ans = 0
        left = 0
        fruit_dict = defaultdict(int)
        for i, val in enumerate(fruits):
            fruit_dict[i] += 1
            while len(fruit_dict) > 2:
                out = fruits[left]
                fruit_dict[out] -= 1
                if fruit_dict[out] == 0:
                    del fruit_dict[out]
                left += 1
            ans = max(ans,i - left + 1)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

if __name__ == '__main__':
    s = "abcd"
    t = "cdef"
    maxCost = 3
    print(f'fun equalSubstring = {equalSubstring(s,t,maxCost)}')

    fruits = [1,2,3,2,2]
    print(f'fun totalFruit = {totalFruit(fruits)}')