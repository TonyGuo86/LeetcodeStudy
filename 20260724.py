'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   7/31/2026 5:38 PM
*  @Project :   Leetcode
*  @FileName:   20260724.py
*  @Function:   tony add
**************************************
'''
import inspect
from collections import defaultdict

from skimage.filters import window

'''
2461. 长度为 K 子数组中的最大和 1553
2461. 长度为 K 子数组中的最大和
study :  defaultdict
'''
def maximumSubarraySum(nums,k):
    try:
        max_val,window_sum = 0,0
        cnt = defaultdict(int)
        for i, val in enumerate(nums):
            window_sum += val
            cnt[val] += 1
            left = i - k + 1
            if left < 0:
                continue
            if len(cnt) == k:
                max_val = max(max_val,window_sum)
            out = nums[left]
            window_sum -= out
            cnt[out] -= 1
            #even one key's value is 0, but len still work, so mwe must del this key
            if cnt[out] == 0:
                del  cnt[out]
        print(cnt)
        return max_val
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


'''
1423. 可获得的最大点数 1574
1423. 可获得的最大点数
'''

'''
由于拿走的点数和 + 剩下的点数和 = 所有点数和 = 常数，所以为了最大化拿走的点数和，应当最小化剩下的点数和。
由于只能从开头或末尾拿牌，所以最后剩下的牌必然是连续的。
至此，问题变成：
计算长为 n−k 的连续子数组和的最小值。
这可以用定长滑动窗口解决

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/solutions/2551432/liang-chong-fang-fa-ni-xiang-si-wei-zhen-e3gb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
def maxScore(cardPoints, k):
    try:
        window_sum = 0
        min_window_sum = float('inf')
        rest_k= len(cardPoints) - k
        if rest_k == 0:
            return sum(cardPoints)
        for i,val in enumerate(cardPoints):
            window_sum += val
            left = i - rest_k + 1
            if left < 0:
                continue
            min_window_sum = min(min_window_sum,window_sum)
            window_sum -= cardPoints[left]
        return sum(cardPoints) - min_window_sum
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


def maxScore_2(cardPoints, k):
    try:
        n = len(cardPoints)
        m = n - k
        min_s = s = sum(cardPoints[:m])
        for i in range(m,n):
            s += cardPoints[i] - cardPoints[i-m]
            min_s = min(min_s,s)
        return sum(cardPoints) - min_s
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')



if __name__ == '__main__':
    nums = [1,5,4,2,9,9,9]
    k = 3
    print(f'maximumSubarraySum ret = {maximumSubarraySum(nums,k)}')

    cardPoints = [9,7,7,9,7,7,9]
    k = 7
    print(f'maxScore ret = {maxScore(cardPoints, k)}')
    print(f'maxScore ret = {maxScore_2(cardPoints, k)}')

