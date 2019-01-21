#!/usr/bin/env python
# coding: utf-8

# In[52]:


# check if two strings are isomorphic
# Given two strings s and t, determine if they are isomorphic. 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# For example,"egg" and "add" are isomorphic, "foo" and "bar" are not.

def isIsomorphic(s,t):
    if (s is None) or (t is None):
        return False
    if len(s) != len(t):
        return False
    map_s = {}
    map_t = {}
    for i,j in enumerate(s):
        if j in map_s:
            if t[i] != map_s[j]:
                return False
        else:
            map_s[j] = t[i]
        if s[i] in map_t:
            if j != map_t[t[i]]:
                print(2)
                return False
        else:
            map_t[t[i]] = j
    return True
# isIsomorphic('foo','baa') 

