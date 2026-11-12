'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   11/10/2026 3:05 PM
*  @Project :   Leetcode
*  @FileName:   20260903.py
*  @Function:   tony add
**************************************
'''


import inspect
import time


def run_time(fun):
    def wrapper(*args,**kwargs):
        start = time.time()
        ret = fun(*args,**kwargs)
        end = time.time()
        print(f'fun={fun.__name__} running time is {end - start}')
        return ret
    return wrapper


'''
34. 在排序数组中查找元素的第一个和最后一个位置
'''

def lower_bound(nums,target):
    left,right = 0,len(nums)-1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] >= target:
            right = middle - 1
        else:
            left = middle + 1
    return left

def upper_bound(nums,target):
    left,right = 0,len(nums)-1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return left

@run_time
def searchRange( nums, target):
    try:
        start = lower_bound(nums,target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        end  = upper_bound(nums,target) - 1
        return [start,end]
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')



'''
35. 搜索插入位置
'''


def searchInsert(nums, target):
    try:
        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')



if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 7
    print(f'fun beautifulBouquet = {searchRange(nums, target)}')

    nums = [1,3,5,6]
    target = 2
    print(f'fun searchInsert = {searchInsert(nums, target)}')