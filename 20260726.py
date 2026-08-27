'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   8/26/2026 5:25 PM
*  @Project :   Leetcode
*  @FileName:   20260726.py
*  @Function:   tony add
**************************************
'''
import inspect

'''
1493. 删掉一个元素以后全为 1 的最长子数组 1423
真如别人所说，删除之后，子数组只有1，也就是没有1，那么删除之前呢？ 至多只有一个0
这个题目的精髓是 你要理解字窗口有一个0就可以，多了就要维护在窗口
'''
def longestSubarray(nums):
    try:
        zero_cnt = 0
        left = 0
        ans = 0
        for right,val in enumerate(nums):
            zero_cnt += 1 -val
            while zero_cnt > 1:
                zero_cnt -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


'''
3634. 使数组平衡的最少移除数目 1453
计算最小的移除数目，所以我们就是要保留最大的数组
滑动窗口
'''
def minRemoval(nums,k):
    try:
        nums.sort()
        left,ans = 0,0
        for right,val in enumerate(nums):
            #找到满足条件的窗口
            while nums[left] * k < right:
                left += 1
            #更新满足条件窗口
            ans = max(ans,right - left + 1)
        return len(nums) - ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

if __name__ == '__main__':
    nums = [0,1,1,1,0,1,1,0,1]
    print(f'fun longestSubarray = {longestSubarray(nums)}')

    nums = [2]
    k = 2
    print(f'fun minRemoval = {minRemoval(nums,k)}')