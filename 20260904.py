'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   11/12/2026 10:47 AM
*  @Project :   Leetcode
*  @FileName:   20260904.py
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
        print(f'fun={fun.__name__} runnine time is {end - start}')
        return ret
    return wrapper



'''
704. 二分查找
'''
@run_time
def search(nums,target):
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
        return -1
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')




'''
744. 寻找比目标字母大的最小字母
'''
@run_time
def nextGreatestLetter(letters, target):
    try:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if ord(letters[mid]) > ord(target):
                right = mid - 1
            else:
                left = mid + 1
        return letters[left] if left != len(letters) else letters[0]
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')



if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 13
    print(f'fun beautifulBouquet = {search(nums, target)}')

    letters = ['x','x','y','y']
    target = 'z'
    print(f'fun nextGreatestLetter = {nextGreatestLetter(letters, target)}')