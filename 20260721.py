'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   7/21/2026 11:14 AM
*  @Project :   Leetcode
*  @FileName:   20260721.py
*  @Function:   tony add
**************************************
'''
import inspect
import math





def maxVowels(s: str, k: int) -> int:
    try:
        vowel,ans = 0,0
        for i,c in enumerate(s):
            if c in 'aeiou':
                vowel += 1
            #判断是不是构成一个完整的窗口
            left = i - k + 1
            if left < 0:
                continue
            #如果构成一个完整的窗口,就获取当前的最大结果
            ans = max(ans,vowel)

            #移动左指针，为下一个循环作准备,假如最左边的是个元音，就需要减去
            if s[left] in 'aeiou':
                vowel -= 1
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


'''
最小值 : float('-inf')
最大值 : float('inf')

'''
def findMaxAverage(nums,k) -> float:
    try:
        window_sum = 0
        ans = float('-inf')
        for i,num in enumerate(nums):
            window_sum += num
            left = i - k + 1
            #如果没有构成一个完整的窗口，就不停的加
            if left < 0:
                continue
            #这里已经构成一个完整的窗口，就开始计算最大的平均值
            ans = max(ans, window_sum / k)
            #需要减去上一个值，为下个循环做准备
            window_sum -= nums[left]
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')



if __name__ == '__main__':
    s = "weallloveyou"
    k = 7
    print(f'maxVowels ret = {maxVowels(s,k)}')

    nums = [-1]
    k = 1
    print(f'findMaxAverage ret = {findMaxAverage(nums,k)}')
