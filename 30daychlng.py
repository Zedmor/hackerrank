# Input Format
#
# There are  lines of numeric input:
# The first line has a double,  (the cost of the meal before tax and tip).
# The second line has an integer,  (the percentage of  being added as tip).
# The third line has an integer,  (the percentage of  being added as tax).
#
# Output Format
#
# Print The total meal cost is totalCost dollars., where  is the rounded integer result of the entire bill ( with added tax and tip).
#
# Sample Input
#
# 12.00
# 20
# 8
# Sample Output
#
# The total meal cost is 15 dollars.
mealCost = 12.0
tipPercent = 20
taxPercent = 8

mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())



totalCost = mealCost + tipPercent/100*mealCost + taxPercent/100*mealCost

print('The total meal cost is '+str(round(totalCost))+' dollars.')


#!/bin/python3

import sys


N = int(input().strip())
if N % 2 != 0:
        print("Weird")
elif (N in range(2,6)) | (N >20):
    print("Not Weird")
else: print("Weird")

N = int(input().strip())
for i in range(N):
    st = str(input().strip())
    str1 = ''
    str2 = ''
    for z in range(len(st)):
        if z%2 == 0:str1+=st[z]
        else: str2+=st[z]
    print(str1,str2)


n = int(input())
yn = ['No','Yes']
for i in range(n):
    print(yn[(int(input()) % 2 == 0])

print(round( 160 +40*(0.88+0.88**2) ,3))
print(round(  128+40*(1.55+1.55**2) ,3))

import math

    ###################################################################################################


    def erf(x):
        ''' John D. Cook's implementation.http://www.johndcook.com
        >> Formula 7.1.26 given in Abramowitz and Stegun.
        >> Formula appears as 1 – (a1t1 + a2t2 + a3t3 + a4t4 + a5t5)exp(-x2)
        >> A little wisdom in Horner's Method of coding polynomials:
            1) We could evaluate a polynomial of the form a + bx + cx^2 + dx^3 by coding as a + b*x + c*x*x + d*x*x*x.
            2) But we can save computational power by coding it as ((d*x + c)*x + b)*x + a.
            3) The formula below was coded this way bringing down the complexity of this algorithm from O(n2) to O(n).'''

        # constants
        a1 = 0.254829592
        a2 = -0.284496736
        a3 = 1.421413741
        a4 = -1.453152027
        a5 = 1.061405429
        p = 0.3275911

        # Save the sign of x
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)

        # Formula 7.1.26 given in Abramowitz and Stegun.
        t = 1.0 / (1.0 + p * x)
        y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * math.exp(-x * x)

        return sign * y


def phi(x):
    '''Cumulative gives a probability that a statistic
    is less than Z. This equates to the area of the
    distribution below Z.
    e.g:  Pr(Z = 0.69) = 0.7549. This value is usually
    given in Z tables.'''

    return 0.5 * (1.0 + erf(x / math.sqrt(2)))


#####################################################################################################

def phi_compcum(x):
    ''' Complementary cumulative gives a probability
    that a statistic is greater than Z. This equates to
    the area of the distribution above Z.
    e.g: Pr(Z  =  0.69) = 1 - 0.7549 = 0.2451'''

    return abs(phi(x) - 1)


#####################################################################################################

def phi_cumformu(x):
    '''Cumulative from mean gives a probability
    that a statistic is between 0 (mean) and Z.
    e.g: Pr(0 = Z = 0.69) = 0.2549'''

    return phi_compcum(0) - phi_compcum(x)

ev,sd=map(int,input().split(' '))

def z(st):
    return((float(st)-ev)/sd)

q1=float(input())
z1=(q1-ev)/sd
print( round( phi(z(input())),2))
strz=input()
print( round( 1-phi(z(input())),2))

z21,z22=map((float-ev)/sd,input().split(' '))
print(round( (1-phi(z21))-(1-phi(z22)),2))


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    return (tuple(aTup[x] for x in range(0,len(aTup),2)))

print (oddTuples((2, 8, 3, 14, 1, 19, 14, 1, 1, 0)))