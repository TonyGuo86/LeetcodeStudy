'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   11/12/2026 9:45 PM
*  @Project :   Leetcode
*  @FileName:   20260905.py
*  @Function:   tony add
**************************************
'''
import inspect

'''
2529. 正整数和负整数的最大计数 
'''
def maximumCount(nums):
    try:
        target = 0
        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        pos_cnt = len(nums) - left
        print(f'pos_cnt = {pos_cnt}')

        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        neg_cnt = right + 1
        print(f'neg_cnt = {neg_cnt}')
        return  max(neg_cnt,pos_cnt)
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

'''
1385. 两个数组间的距离值 1235
'''
def findTheDistanceValue(arr1, arr2, d):
    try:
        ans = 0
        sort_arr2 = sorted(arr2)
        for i in range(len(arr1)):
            left,right = 0,len(sort_arr2)-1
            while left <= right:
                mid = (left + right) // 2
                if sort_arr2[mid] >= arr1[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(sort_arr2):
                left_target = sort_arr2[len(sort_arr2)-1]
                right_target = sort_arr2[len(sort_arr2) - 1]
            else:
                left_target = sort_arr2[left]
                right_target = sort_arr2[right]
            if abs(arr1[i] - left_target) > d and abs(arr1[i] - right_target) > d:
                ans += 1
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

if __name__ == '__main__':
    nums = [0,0]
    print(f'fun maximumCount = {maximumCount(nums)}')

    arr1 = [-803,715,-224,909,121,-296,872,807,715,407,94,-8,572,90,-520,-867,485,-918,-827,-728,-653,-659,865,102,-564,-452,554,-320,229,36,722,-478,-247,-307,-304,-767,-404,-519,776,933,236,596,954,464]
    arr2 = [817,1,-723,187,128,577,-787,-344,-920,-168,-851,-222,773,614,-699,696,-744,-302,-766,259,203,601,896,-226,-844,168,126,-542,159,-833,950,-454,-253,824,-395,155,94,894,-766,-63,836,-433,-780,611,-907,695,-395,-975,256,373,-971,-813,-154,-765,691,812,617,-919,-616,-510,608,201,-138,-669,-764,-77,-658,394,-506,-675,523,730,-790,-109,865,975,-226,651,987,111,862,675,-398,126,-482,457,-24,-356,-795,-575,335,-350,-919,-945,-979,611]
    d = 37
    print(f'fun findTheDistanceValue = {findTheDistanceValue(arr1,arr2,d)}')