#!/usr/bin/env python3
''' this modules computes the pascal triangle using a function called pascal_triangle'''


def pascal_triangle(n):
    '''computes pascal triangle or 
return an empty list if n <= 0'''
    r = 0;
    k = n-1;
    j = 0
    pascal_array = []
    pascal_next = []
    if (n <= 0):
        return [];
    while (j < n):
        i = 0
        while (i < j):
            if (j == 0):
                pascal_next.append(1)
            elif (j == 1):
                pascal_next.extend([1,1])
            elif j > 1 :
                if i >= 2 and i < j-1: 
                    pascal_next.append(pascal_array[j][i-1] + pascal_array[j][i])
                else:
                    pascal_next.append(pascal_array[j][i])
            i += 1
        pascal_next.append(1)    
        pascal_array.append(pascal_next)
        print(pascal_next)
        j += 1
    return pascal_array

    

