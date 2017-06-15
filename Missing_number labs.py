def find_missing(arr1, arr2):

    # Set longer array to lst1, shorter to lst2 
    if len(arr1) > len(arr2):
        lst1 = arr1
        lst2 = arr2
    else:
        lst1 = arr2
        lst2 = arr1

    # Go through elements in longer list
    for element in lst1:

        # If this element is not in lst2, we found it, return result
        if element not in lst2:
            return element
print(find_missing([12,3,6],[12,6])) 
           