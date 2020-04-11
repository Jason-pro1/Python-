def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[i] < alist[min_index]:
                min_index = i
        if j != min_index:
            alist[j], alist[min_index] = alist[min_index], alist[j]

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)
    print("最优时间复杂度O（n^2）； 最坏时间复杂度O（n^2）；稳定性：不稳定(考虑升序每次选择最大的情况)")
