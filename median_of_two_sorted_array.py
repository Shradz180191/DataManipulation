# Median of two sorted array

def get_median(array1, array2):
    if (len(array1) == 0) and (len(array2) != 0):
        return array2[int(len(array2)/2)]
    else:
        if (len(array2) == 0) and (len(array2) != 0):
            return array1[int(len(array1)/2)]
        else:
            array1.extend(array2)
            array1.sort()
            return array1[int(len(array1)/2)]
        
# arr1 = [1,2,4,6,8,10]
# arr2 = [3,5,6,7,9,11]
# get_median(arr1,arr2)
