'''
Created on Nov 20, 2015

@author: lucie
'''
#Write a function that accepts a number and returns the number at that position in the fibonnaci sequence.
def fibR(n):
    if n==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibR(n-1)+fibR(n-2)
    
def fibM(n):
    memo = {0:0, 1:1}
    if not n in memo:
        memo[n] = fibM(n-1) + fibM(n-2)
    return memo[n]

print fibR(7)
print fibM(7)