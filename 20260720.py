'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   7/20/2026 12:35 PM
*  @Project :   Leetcode
*  @FileName:   20260720.py
*  @Function:   tony add
**************************************
'''
import inspect
import math
'''
given an array of integers nums and an integer target, return indices of the 
two numbers such that ann up to target.
'''


def twoSum(nums,target):
    try:
        mydic = {}
        mydic[nums[0]] = 0
        for i in range(1,len(nums)):
            if target - nums[i] in list(mydic.keys()):
                return i,mydic[target - nums[i]]
            else:
                mydic[nums[i]] = i
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

'''
1 跟 任何数得最小公倍数是他本身
0 跟 任何书得最大共因数是他本身
'''
def maxLength(nums):
    try:
        ans = 0
        for i in range(0,len(nums)):
            m,g,l = 1,0,1
            for j in range(i,len(nums)):
                m *= nums[j]
                l = math.lcm(l,nums[j])
                g = math.gcd(g, nums[j])
                if l * g == m:
                    ans = max(ans,j-i+1)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


if __name__ == '__main__':
    nums = [3,3]
    target = 6
    ret = twoSum(nums,target)
    print(f'twoSum ret = {ret}')

    nums = [2,6]
    ret = maxLength(nums)
    print(f'maxLength ret = {ret}')


    lcm = math.lcm(1,12)
    print(f'lcm = {lcm}')

    gcd = math.gcd(0,34)
    print(f'gcd = {gcd}')