'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   7/31/2026 4:31 PM
*  @Project :   Leetcode
*  @FileName:   20260723.py
*  @Function:   tony add
**************************************
'''
import inspect
'''
2379. 得到 K 个黑块的最少涂色次数 1360
'''
def minimumRecolors(blocks, k):
    try:
        min_cnt = float('inf')
        b_cnt = 0
        for i,c in enumerate(blocks):
            if c == 'B':
                b_cnt += 1
            left = i - k + 1
            if left < 0:
                continue
            min_cnt = min(k-b_cnt,min_cnt)
            if blocks[left] == 'B':
                b_cnt -= 1
        return min_cnt
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


'''
2841. 几乎唯一子数组的最大和 1546
'''
def maxSum(nums, m, k):
    try:
        max_sum = 0
        sub_list = []
        for i,val in enumerate(nums):
            sub_list.append(val)
            left = i - k + 1
            if left < 0:
                continue
            if len(set(sub_list)) >= m:
                max_sum =max(max_sum,sum(sub_list))
            sub_list.pop(0)
        return max_sum
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

if __name__ == '__main__':
    blocks = "WBWBBBW"
    k = 2
    print(f'minimumRecolors ret = {minimumRecolors(blocks,k)}')

    nums = [2, 6, 7, 3, 1, 7]
    m = 3
    k = 4
    print(f'maxSum ret = {maxSum(nums,m,k)}')
