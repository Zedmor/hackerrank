# Correlation and Regression Lines - A Quick Recap #1
# by PRASHANTB1984
# Problem
# Submissions
# Leaderboard
# Discussions
# Here are the test scores of 10 students in physics and history:
#
# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15
# Compute Karl Pearson’s coefficient of correlation between these scores.
# Compute the answer correct to three decimal places.
#
# Output Format
#
# In the text box, enter the floating point/decimal value required. Do not leave any leading or trailing spaces. Your answer may look like: 0.255
#
# This is NOT the actual answer - just the format in which you should provide your answer.

import numpy as np
import math
s1 = "15  12  8   8   7   7   7   6   5   3"
s2 = "10  25  17  11  13  17  20  13  9   15"

X = np.array(list(map(int, s1.split())))
Y = np.array(list(map(int, s2.split())))

def mean(list):
    return sum(list)/len(list)



sum(
    np.array([(x-mean(X)) for x in X])*np.array([(y-mean(Y)) for y in Y])
)/\
(math.sqrt(sum(np.array([(x-mean(X))**2 for x in X]))) *\
math.sqrt(sum(np.array([(x-mean(Y))**2 for x in Y])))
 )


#Day 5: Poisson Distribution I
def fact(x):
    factorial = 1
    for i in range(1, x + 1):
        factorial *= i
    return factorial


def pua(k, lamb):
    e = 2.71828
    return (((lamb ** k) * (e ** -lamb)) / fact(k))


print(round(pua(1, 0.88), 3))

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

# Your Code Here
testList = [1, -4, 8, -9]
print(applyToEach(testList,int)+1)


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    z=''
    x=0
    for i in aDict.keys():
       if len(aDict[i])>x: x=len(aDict[i]);z=i
    return(z)

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

biggest(animals)