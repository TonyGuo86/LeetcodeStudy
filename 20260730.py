'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   8/31/2026 11:07 AM
*  @Project :   Leetcode
*  @FileName:   20260730.py
*  @Function:   tony add
**************************************
'''
import inspect
from collections import defaultdict

'''
209. 长度最小的子数组
'''
def minSubArrayLen(target,nums):
    try:
        ans,left,windows_sum = float('inf'),0,0
        for right,val in enumerate(nums):
            windows_sum += val
            while windows_sum >= target:
                ans = min(ans, right - left + 1)
                windows_sum -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},error={e.__traceback__.tb_lineno},error={e}')



'''
3795. 不同元素和至少为 K 的最短子数组长度 1505
'''
def minLength(nums, k):
    try:
        ans,left,window_sum = float('inf'),0,0
        cnt_dict = defaultdict(int)
        for right,val in enumerate(nums):
            cnt_dict[val] += 1
            if cnt_dict[val] == 1:
                window_sum += val
            while window_sum >= k:
                ans = min(ans,right - left + 1)

                #最精髓的一点是这里
                out = nums[left]
                cnt_dict[out] -= 1
                if cnt_dict[out] == 0:
                    window_sum -= out
        return -1 if ans == float('inf') else ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},error={e.__traceback__.tb_lineno},error={e}')

if __name__ == '__main__':
    target = 7
    nums = [2,3,1,2,4,3]
    print(f'fun minSubArrayLen = {minSubArrayLen(target, nums)}')

    nums = [5,5,4]
    k = 5
    print(f'fun minLength = {minLength(nums, k)}')

