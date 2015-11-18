'''
Created on Nov 18, 2015

@author: lucie
'''
#  Using Python, have a function that takes in a sentence
#  being passed and return the largest word in the string. If there are two or more 
#  words that are the same length, return the first word from the string with that length.
#  Ignore punctuation and assume sentence will not be empty. 

def largest(sent):
    array = sent.split()
    largestWord = max(array, key=len)
    print (array)
    return largestWord
    
print (largest("I love macaroni and cheese"))