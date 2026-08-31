'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   8/28/2026 5:25 PM
*  @Project :   Leetcode
*  @FileName:   20260729.py
*  @Function:   tony add
**************************************
'''
import inspect
from collections import defaultdict

'''
2024. 考试的最大困扰度 1643
'''
def maxConsecutiveAnswers(answerKey, k):
    try:
        ans,left = 0,0
        cnt = defaultdict(int)
        for right,c in enumerate(answerKey):
            cnt[c] += 1
            while cnt['T'] > k and cnt['F'] > k:
                cnt[answerKey[left]] -= 1
                left += 1
            ans = max(ans,right - left + 1)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


'''
1004. 最大连续 1 的个数 III 1656
'''
def longestOnes(nums, k):
    try:
        ans,left = 0,0
        cnt = defaultdict(int)
        for right,value in enumerate(nums):
            cnt[value] += 1
            while cnt[0] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans,right - left + 1)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

if __name__ == '__main__':
    answerKey = "TFFT"
    k = 1
    print(f'fun maxConsecutiveAnswers = {maxConsecutiveAnswers(answerKey, k)}')

    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(f'fun longestOnes = {longestOnes(nums, k)}')