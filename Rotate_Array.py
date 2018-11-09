#!/usr/bin/env python
# coding: utf-8

# In[1]:


#program to rotate an array to left by given number of times
def rotate_arr_left(arr,rot_fact):
    n = len(arr)
    for x in range(rot_fact):
        temp = arr[0]
        for y in range(0,n-1):
            arr[y] = arr[y + 1]
            
        arr[n - 1] = temp
    return arr    
ar = [1,2,3,4,5,6,7,8,9,10]
factor = 4
rotate_arr_left(ar,4)

        


# In[2]:


#program to rotate an array to the right by given number of times
def rotate_arr_right(arr,rot_fact):
    n = len(arr)
    for x in range(rot_fact):
        temp = arr[n - 1]
        for y in range(0,n-1):
            arr[y + 1] = ar[y]
        
        arr[0] = temp
    return arr

r = [1,2,3,4,5,6,7,8,9,10]
factor = 4
rotate_arr_left(ar,4)

