'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   11/16/2026 3:14 PM
*  @Project :   Leetcode
*  @FileName:   20260907.py
*  @Function:   tony add
**************************************
'''
import bisect
import inspect

from pathlib import Path
from collections import  *


'''
2389. 和有限的最长子序列 非暴力做法
'''
def answerQueries(nums, queries):
    try:
        ans = []
        sorted_nums = sorted(nums)
        for target in queries:
            win_sum = 0
            length = 0
            for i,val in enumerate(sorted_nums):
                win_sum += val
                if win_sum > target:
                    win_sum -= val
                    continue
                length += 1
            ans.append(length)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')



'''
2080. 区间内查询数字的频率 1702
'''
class RangeFreqQuaery:
    def __init__(self,arr):
        self.arr = arr
    def query(self,left,right,value):
        try:
            sub = self.arr[left:right+1]
            counter = Counter(sub)
            ans = counter[value]
            return ans
        except Exception as e:
            print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

class RangeFreqQuaery_good:
    def __init__(self,arr):
        #统计每个元素的下标
        self.pos = defaultdict(list)
        for i,x in enumerate(arr):
            self.pos[x].append(i)

    def query(self,left,right,value):
        try:
            #找到这个元素的下标列表
            sub = self.pos[value]
            right = bisect.bisect_right(sub,right)
            left = bisect.bisect_left(sub,left)
            return right - left
        except Exception as e:
            print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


if __name__ == '__main__':
    nums = [469781,45635,628818,324948,343772,713803,452081]
    queries = [816646,929491]
    print(f'fun answerQueries = {answerQueries(nums, queries)}')

    rangeFreqQuery = RangeFreqQuaery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
    ans = rangeFreqQuery.query(1, 2, 4)
    print(f'ans = {ans}')

    ans = rangeFreqQuery.query(0, 11, 33)
    print(f'ans = {ans}')


    sub = [1,4,6,7]
    left = bisect.bisect_left(sub,2)
    print(f'left = {left}')

    right = bisect.bisect_right(sub,5)
    print(f'right = {right}')


