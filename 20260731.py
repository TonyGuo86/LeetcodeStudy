'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   8/31/2026 3:17 PM
*  @Project :   Leetcode
*  @FileName:   20260731.py
*  @Function:   tony add
**************************************
'''
import inspect

from collections import  Counter

'''
2904. 最短且字典序最小的美丽子字符串 做到 O(n^2)
'''
def shortestBeautifulSubstring(s, k):
    try:
        if s.count('1') < k:
            return ''
        ans = s
        left,cnt_one = 0,0
        for right,c in enumerate(s):
            cnt_one += int(s[right])
            while cnt_one > k or s[left] == '0':
                cnt_one -= int(s[left])
                left += 1
            if cnt_one == k:
                temp = s[left:right+1]
                if len(temp) < len(ans) or len(temp) == len(ans) and temp < ans:
                    ans = temp
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')



'''
1234. 替换子串得到平衡字符串 1878
'''
def balancedString(s):
    try:
        s1 = 'QQQQ'
        s2 = 'QERW'

        cnt = Counter(s2)
        print(len(cnt))
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

if __name__ == '__main__':
    s = "100011001"
    k = 3
    print(f'fun shortestBeautifulSubstring = {shortestBeautifulSubstring(s, k)}')


    s = "QQWE"
    print(f'fun balancedString = {balancedString(s)}')

