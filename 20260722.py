'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   7/31/2026 3:26 PM
*  @Project :   Leetcode
*  @FileName:   20260722.py
*  @Function:   tony add
**************************************
'''
import inspect

'''
滑动窗口的code
1343. 大小为 K 且平均值大于等于阈值的子数组数目 1317
'''
def numOfSubarrays(arr,k,threshold) -> int:
    try:
        ans = 0
        windows_sum = 0
        for i,num in enumerate(arr):
            windows_sum += num
            left = i - k + 1
            if left < 0:
                continue
            ans += 1 if windows_sum / k >= threshold else 0
            windows_sum -= arr[left]
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

'''
2090. 半径为 k 的子数组平均值 1358
'''
def getAverages(nums, k):
    try:
        ret = []
        window_sum = 0
        for i,num in enumerate(nums):
            '''
            判断左右指针是否超过了界限
            '''
            left = i - k
            right = i + k
            if left < 0:
                ret.append(-1)
            elif right > len(nums) - 1:
                ret.append(-1)
            else:
                '''
                left 等于0的时候说明是第一次，就计算这个的和
                '''
                if left == 0:
                    window_sum = sum(nums[left:right+1])
                    ret.append(window_sum // (right - left + 1))
                else:
                    '''
                    不等于0的时候，就只是右指针移动了一位，加上就行了
                    '''
                    window_sum += nums[right]
                    ret.append(window_sum // (right - left + 1))
                window_sum -= nums[left]
        return ret
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


if __name__ == '__main__':
    arr = [11,13,17,23,29,31,7,5,2,3]
    k = 3
    threshold = 5
    print(f'numOfSubarrays ret ={numOfSubarrays(arr,k,threshold)}')

    nums = [7,4,3,9,1,8,5,2,6]
    k = 3
    print(f'getAverages ret ={getAverages(nums,k)}')
