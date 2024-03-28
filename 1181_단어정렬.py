import sys, heapq
from typing import MutableSequence


# N = 5
#li = ['asdf','asd','z','d','f','a','fd','as','hg','eg','yj','er','cv','sd']


def qsort_len(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 요소)

    while pl <= pr:    # 실습 6-10과 같은 while 문
        while len(a[pl]) < len(x): pl += 1
        while len(a[pr]) > len(x): pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort_len(a, left, pr)
    if pl < right: qsort_len(a, pl, right)

def quick_sort_len(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort_len(a, 0, len(a) - 1)
    
def quick_sort_str(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 요소)

    while pl <= pr:    # 실습 6-10과 같은 while 문
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: quick_sort_str(a, left, pr)
    if pl < right: quick_sort_str(a, pl, right)

def quick_sort_len(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort_len(a, 0, len(a) - 1)

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    x = [sys.stdin.readline().rstrip() for i in range(N)]
    x = set(x)
    x = list(x)
    quick_sort_len(x)      # 배열 x를 퀵 정렬

        # 길이가 같은 문자열끼리 사전 순으로 정렬
    i = 0
    while i < len(x):
        length_group_start = i
        current_length = len(x[i])
        while i < len(x) and len(x[i]) == current_length:
            i += 1
        quick_sort_str(x, length_group_start, i - 1)
    
    for string in x:
        print(string)
