def binarysearch (list, item):
    first = 0
    last = len(list) - 1
    found = False
    while not found and first <= last:
        mid = (first+last)//2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

x = [1,2,3,4,5,6,7,8,9]
y = 2

print(binarysearch(x, y))
