'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   8/26/2026 4:11 PM
*  @Project :   Leetcode
*  @FileName:   20260725.py
*  @Function:   tony add
**************************************
'''
import inspect
from collections import defaultdict

'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

def lengthOfLongestSubstring(s):
    try:
        ans = 0
        window_str = []
        for i,ch in enumerate(s):
            if ch not in window_str:
                window_str.append(ch)
            else:
                ans = max(ans,len(window_str))
                window_str = window_str[window_str.index(ch)+1:]
                window_str.append(ch)
        return max(len(window_str),ans)
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

def lengthOfLongestSubstring_2(s):
    try:
        ans = left = 0
        cnt = defaultdict(int)
        for right,c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')

'''
3090. 每个字符最多出现两次的最长子字符串 1329
给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该子字符串的 最大 长度
'''
def maximumLengthSubstring(s):
    try:
        ans = left = 0
        cnt = defaultdict(int)
        for right,c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 2:
                cnt[s[left]] -= 1 #一直找到重复大于2个字符的left
                left += 1
            ans = max(ans,right - left + 1)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')



if __name__ == '__main__':
    s = "pwwkew"
    print(f'fun lengthOfLongestSubstring = {lengthOfLongestSubstring(s)}')
    print(f'fun lengthOfLongestSubstring_2 = {lengthOfLongestSubstring_2(s)}')

    s = "aaaa"
    print(f'fun maximumLengthSubstring = {maximumLengthSubstring(s)}')




