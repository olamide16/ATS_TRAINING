def binarySearch(arr,element):
    low = 0
    high = len(arr)-1
    if_found = False
    while( low<=high and not if_found):
        mid = (low + high)//2
        
        if arr[mid] == element :
            if_found = True
        else:
            if element < arr[mid]:
                high = mid - 1
            else:
                 low = mid + 1
    if if_found==True:
        return("Element {} found at index".format(element),mid)
    else:
        return("Element {} Not found".format(element))