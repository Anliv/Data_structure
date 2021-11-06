#!/usr/bin/env python
# coding: utf-8

# In[4]:


def bubblesort(sort_list):
    n = len(sort_list)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if sort_list[j] > sort_list[j + 1] :
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
 
sort_list = [5, 1, 4, 2, 8]
 
# test the result
bubblesort(sort_list)
print (sort_list)


# In[ ]:


#Best case - the list was sorted already, the run-time complexity is O(n); the first loop is run n time, without any processing in the loop because the condition results in False
#Worst case - the list was not sorted, the complexity is O(n x n) (or O(n^2)); in the 1st search, the algorithm needs to run (n-1) time; in 2nd search, the algorithm needs to run (n-2) time
# hence in the worse case, the total run-time is (n-1) + (n-2) + (n-3) +... + 2 + 1  = O (n^2)

