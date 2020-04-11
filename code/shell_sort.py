# 希尔排序
def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = gap
            while (i-gap) >= 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)
    print("最优时间复杂度:根据步长序列的不同而不同； 最坏时间复杂度O（n^2）；稳定性：不稳定")    
