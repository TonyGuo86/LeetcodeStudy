'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   11/9/2026 4:25 PM
*  @Project :   Leetcode
*  @FileName:   20260902.py
*  @Function:   tony add
**************************************
'''
import inspect
import queue
import time
from collections import Counter, defaultdict
from email.policy import default


def run_time(fun):
    def wrapper(*args,**kwargs):
        start = time.time()
        ret = fun(*args,**kwargs)
        end = time.time()
        print(f'{fun.__name__} running time is {end - start:0.4f}')
        return ret
    return wrapper
'''
LCP 68. 美观的花束
'''
def beautifulBouquet(flowers, cnt):
    try:
        ans,left = 0,0
        counter = Counter()
        for right, val in enumerate(flowers):
            counter[val] += 1
            while counter[val] > cnt:
                out = flowers[left]
                counter[out] -= 1
                if counter[out] == 0:
                    del  counter[out]
                left += 1
            ans += right - left + 1
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')



'''
1358. 包含所有三种字符的子字符串数目 1646
这个题的精髓 :  此时，我们把左端点移动到了一个「恰好」不合法的位置。什么是「恰好」？就是说 [left,right] 
这个子串是不符合要求的，但 [left−1,right] 是符合要求的。由于子串越长越符合要求，
所以除了 [left−1,right] 符合要求，更长的 [left−2,right],[left−3,right],…,[0,right] 也符合要求。
所以当右端点固定在 right 时，左端点在 0,1,2,…,left−1 的所有子串都是符合要求的，这一共有 left 个，加到答案中
'''
@run_time
def numberOfSubstrings(s):
    try:
        ans,left = 0,0
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
            while len(cnt) == 3:
                out = s[left]
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            ans += left
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


if __name__ == '__main__':
    flowers = [5,3,3,3]
    cnt = 2
    print(f'fun beautifulBouquet = {beautifulBouquet(flowers, cnt)}')

    s = "abcabc"
    print(f'fun numberOfSubstrings = {numberOfSubstrings(s)}')