'''
**************************************
*  @Author  ：   tonyguo@gopro.com
*  @Time    ：   11/16/2026 11:29 AM
*  @Project :   Leetcode
*  @FileName:   20260906.py
*  @Function:   tony add
**************************************
'''
import inspect
import bisect
from collections import Counter

from sklearn.utils.arrayfuncs import min_pos

'''
1170. 比较字符串最小字母出现频次 1432
'''
def numSmallerByFrequency(queries, words):
    try:
        numbers = []
        for word in words:
            word_counter = Counter(word)
            word_frequency = word_counter[min(word_counter)]
            numbers.append(word_frequency)
        ans = []
        for query in queries:
            query_counter = Counter(query)
            query_frequency = query_counter[min(query_counter)]
            print(f'source is {query} min character is {min(query_counter)},frequency is {query_frequency}')

            ret = 0
            for i in numbers:
                if query_frequency < i:
                    ret += 1
            ans.append(ret)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


'''
2300. 咒语和药水的成功对数 1477
'''


def successfulPairs(spells, potions, success):
    try:
        ans = []
        sorted_potions = sorted(potions)
        print(sorted_potions)
        for spell in spells:
            target = success / spell
            idx = bisect.bisect_left(sorted_potions,target)
            ans.append(len(sorted_potions) - idx)
        return ans
    except Exception as e:
        print(f'fun={inspect.stack()[0][3]},line={e.__traceback__.tb_lineno},error={e}')


if __name__ == '__main__':
    queries = ['cbd']
    words = ['zaaaz']
    print(f'fun numSmallerByFrequency = {numSmallerByFrequency(queries,words)}')

    spells = [5,1,3]
    potions = [1,2,3,4,5]
    success =7
    print(f'fun successfulPairs = {successfulPairs(spells, potions,success)}')

    a = [5,8,8]
    b = bisect.bisect_right(a,5)
    print(b)