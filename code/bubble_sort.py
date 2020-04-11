# 冒泡排序
def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
#         j [0, 1, 2, ...n-2]
#         n-2-j
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)
    print("最优时间复杂度O（n）； 最坏时间复杂度O（n^2）；稳定性：稳定")
