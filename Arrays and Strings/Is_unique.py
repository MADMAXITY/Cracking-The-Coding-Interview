def solution_nlogn(arr):
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:return False
    return True



def solution_extra_space(arr):
    hashmap = {}
    for i in arr:
        if i in hashmap:return False
        hashmap[i] = True
    return True


S = [x for x in input("Give a string : ")]

ans_extra_space = solution_extra_space(S)
ans_nlogn = solution_nlogn(S)
print(ans_extra_space)
print(ans_nlogn)
