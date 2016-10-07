def quickSort(array):
    lessThan = []
    equalTo = []
    greaterThan = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                lessThan.append(x)
            if x == pivot:
                equalTo.append(x)
            if x > pivot:
                greaterThan.append(x)
        return quickSort(lessThan)+equalTo+quickSort(greaterThan)
    else:
        return array

def mergeSort(array):
    resultArray = []
    if len(array) < 20:
        # is this cheating???
        return sorted(array)
    midPoint = int(len(array)/2)
    y = mergeSort(array[:midPoint])
    z = mergeSort(array[midPoint:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            resultArray.append(z[j])
            j += 1
        else:
            resultArray.append(y[i])
            i += 1
    resultArray += y[i:]
    resultArray += z[j:]
    return resultArray
print quickSort([12,4,4,5,67,8,65,7,756,7,675,67,734,543,234,8790,3243,980,4234,5,6,78,30,1,4,-3,7,3,1,15])
print mergeSort([12,4,4,5,67,8,65,7,756,7,675,67,734,543,234,8790,3243,980,4234,5,6,78,30,1,4,-3,7,3,1,15])
