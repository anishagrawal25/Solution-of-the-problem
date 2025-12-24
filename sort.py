#Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

n = int(input())
arr = list(map(int,input().split()))



print(is_sorted(arr))
