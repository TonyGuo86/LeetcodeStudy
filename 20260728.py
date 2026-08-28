'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   8/28/2026 3:55 PM
*  @Project :   Leetcode
*  @FileName:   20260728.py
*  @Function:   tony add
**************************************
'''
import inspect
from collections import defaultdict

'''
1695. 删除子数组的最大得分 1529
'''
def maximumUniqueSubarray(nums):
    try:
        ans,left = 0,0
        myset = set()
        window_sum = 0
        for i, val in enumerate(nums):
            while val in myset:
                myset.remove(nums[left])
                window_sum -= nums[left]
                left += 1
            myset.add(val)
            window_sum += val
            ans = max(ans,window_sum)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


'''
2958. 最多 K 个重复元素的最长子数组 1535
'''
def maxSubarrayLength(nums,k):
    try:
        ans,left = 0,0
        temp_dict = defaultdict(int)
        for i ,val in enumerate(nums):
            temp_dict[val] += 1
            while temp_dict[val] > k:
                out = nums[left]
                temp_dict[out] -= 1
                if temp_dict[out] == 0:
                    del temp_dict[out]
                left += 1
            ans = max(ans,i-left+1)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


if __name__ == '__main__':
    nums = [4,2,4,5,6]
    print(f'fun maximumUniqueSubarray = {maximumUniqueSubarray(nums)}')

    nums = [5,5,5,5,5,5,5]
    k = 4
    print(f'fun maxSubarrayLength = {maxSubarrayLength(nums,k)}')




