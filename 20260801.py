'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   10/30/2026 2:39 PM
*  @Project :   Leetcode
*  @FileName:   20260801.py
*  @Function:   tony add
**************************************
'''
import inspect

from skimage.filters import window

'''
2875. 无限数组的最短子数组 1914
这个题你真的需要学会的是化繁为简 : target = n * len(nums) + reminder 
为啥要执行2遍呢，因为你要包含所有的数据  right % len(nums)
'''
def minSizeSubarray(nums, target):
    try:
        total = sum(nums)
        window_sum, left = 0,0
        cycles,reminder = divmod(target,total)
        n = len(nums)
        best = n
        for right in range(n * 2):
            window_sum += nums[right % n]
            while window_sum >= reminder:
                if window_sum == reminder:
                    best = min(best,right - left + 1)
                window_sum -= nums[left % n]
                left += 1
        return cycles * n + best if best < n else -1
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')



'''
713. 乘积小于 K 的子数组
给定一个整数数组 nums 和一个整数 k。
请你返回 子数组 内所有元素的 乘积严格小于 k 的连续子数组的数目
理解这样 [a,b] = [a,a],[a,a+1],[a,a+1,a+2]...... ===> 可以看出个数的a,a+1,a+2,......, a+right === right - left + 1 
'''

def numSubarrayProductLessThanK(nums,k):
    try:
        product_sum,left = 1,0
        ans = 0
        for right,val in enumerate(nums):
            product_sum *= val
            while product_sum >= k and left <= right:
                product_sum //= nums[left]
                left += 1
            ans += (right - left + 1)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


if __name__ == '__main__':
    nums = [1,1,1,2,3]
    target = 4
    print(f'fun minSizeSubarray = {minSizeSubarray(nums, target)}')

    nums = [1,2,3]
    k = 0
    print(f'fun numSubarrayProductLessThanK = {numSubarrayProductLessThanK(nums, k)}')