def urlify(arr,n):
    arr = [x for x in arr]
    i = len(arr)-1
    cur = n-1
    while cur>=0:
        if arr[cur]!=' ':
            arr[i] = arr[cur]
            i-=1
            cur-=1
        else:
            arr[i] = '0'
            arr[i-1] = '2'
            arr[i-2] = '%'
            i-=3
            cur-=1
    return ''.join(arr)


s,n = "Mr John Smith    ",13
print(urlify(s,n))
