'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   11/4/2026 11:13 PM
*  @Project :   Leetcode
*  @FileName:   20260901.py
*  @Function:   tony add
**************************************
'''
import inspect
from collections import Counter


'''
3258. 统计满足 K 约束的子字符串数量 I 做到 O(n)
'''

def countKConstraintSubstrings(s, k):
    try:
        one_cnt,zero_cnt = 0,0
        ans,left = 0,0
        for right,c in enumerate(s):
            one_cnt += int(c)
            zero_cnt += 1 - int(c)
            while one_cnt > k and zero_cnt > k:
                one_cnt -= int(s[left])
                zero_cnt -= 1  - int(s[left])
                left += 1
            ans += right - left + 1
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

'''
2762. 不间断子数组 1940
'''

def continuousSubarrays(nums):
    try:
        if len(nums) < 2:
            return len(nums)
        ans,left = 0,0
        cnt = Counter()
        for right,val in enumerate(nums):
            cnt[val] += 1
            while max(cnt) - min(cnt) > 2:
                out = nums[left]
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            ans += right - left + 1
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')




if __name__ == '__main__':
    s = "11111"
    k = 1
    print(f'fun minSizeSubarray = {countKConstraintSubstrings(s, k)}')

    nums = [5,4,2,4]
    print(f'fun continuousSubarrays = {continuousSubarrays(nums)}')

