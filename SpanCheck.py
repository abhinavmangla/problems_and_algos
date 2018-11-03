#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#program to give the largest span between any two equal elements in an array

def spancheck(nums):
    span = 0;
    maxi = 0;
    n = len(nums)
    for x in range(0,n):
        curr_element = nums[x]
        for y in range(x + 1,n):
            if(nums[y] == curr_element):
                print(nums[y])
                span = y - x - 1;
                maxi = span
        
    return maxi


a = [1,2,3,4,5,2,1]
spancheck(a)

