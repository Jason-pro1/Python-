# 快速排序
def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:
        return 
    mid = alist[start]
    left = start
    right = end
    
    while left < right:
        while left < right and alist[right]  >= mid:
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] < mid:
            left += 1
        alist[right] = alist[left]
#      从循环退出后，left与right相遇，即left == right
    alist[left] = mid
    
    quick_sort(alist, start, left-1) 
    quick_sort(alist, left+1, end)
    
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)
    print("最优时间复杂度:O(nlogn)； 最坏时间复杂度O（n^2）；稳定性：不稳定") 

        
