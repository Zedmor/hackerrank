#!/usr/bin/python
# Your submission will run against only preliminary test cases. Full test cases will run at the end of the day.
# lighthouse
#
# CubeCraft is a game consisting entirely of cubes (or voxels) having a side length equal to , and each voxel's vertices have integer coordinates. After playing this game for a while,
# Jessie is eager to create something impressive so she decides to build a lighthouse.
#
# First, Jessie decides she wants the lighthouse to have a round base; because there is no such thing as a perfect circle in a cubic world,
#  she defines a circle with integer radius r to be the set of all cubes having centers with a Euclidean distance to the center of the circle (which coincides with the center of some cube) <=r .
#  Because r is the Euclidean distance between the center points of two cubes, the value of  for a single cube is 0.
#
# Next, she chooses an n x n grid for the base of the lighthouse. This presents some difficulty for Jessie because there are landscape features
# (e.g., rocks, trees, etc.) in the grid. She doesn't want to change the landscape and cannot build over it, so she must find the maximum
# radius of any circle she can place inside the grid's free space (i.e., where no landscape obstructions are contained within the confines of the circle).
#  Note that circle have to be placed completely inside the grid, i.e. there should be no points with euclidean distance to the center  <= outside the grid.
#
# Given n and the landscape features of Jessie's grid, find and print the maximum possible value of r.
#
# Input Format
#
# The first line contains an integer, n, denoting the side dimensions of the grid where Jessie wants to build the lighthouse.
# Each line i of the n subsequent lines contains a string of n characters describing the landscape features of row i in the grid. A . indicates that (i,j,1) is empty, and a * indicates that it's obstructed.
#
# Constraints
#1<=n<=50
#
# It is guaranteed that the grid contains at least one empty cell (i.e., input will always contain at least one . character).
# Output Format
#
# Print the value of r denoting the maximum integer radius of the circle Jessie can place inside the grid's free space (recall that r  may be 0).
#
# Sample Input 0
#
# 9
# *********
# ****.****
# **.....**
# **.....**
# *.......*
# **.....**
# **.....**
# ****.****
# *********
# Sample Output 0
#
# 3
# Explanation 0
# Build a lighthouse with radius  at the center of the grid. Note that it will fill ALL free cells.
#
# Sample Input 1
#
# 5
# .*.*.
# *...*
# .....
# *...*
# .*.*.
# Sample Output 1
#
# 2
# Explanation 1
# Build a lighthouse with radius  at the center of the grid.
#
# Sample Input 2
#
# 5
# ***.*
# **..*
# ***.*
# *****
# *****
# Sample Output 2
#
# 0
import math

f = open("lighthouse.txt","r")
#We using file lighthouse.txt as input for tests
n=int(f.readline())

pic=[]
mtrx = f.read().splitlines()

#convert it to int matrix, 0 = free, 1 = occupied
for i in range(n):
     mtrx[i]=mtrx[i].replace(".","0");mtrx[i]=mtrx[i].replace("*","1")
     mtrx[i]=list(map(int,mtrx[i]))

mtrx=mtrx[:n]


'''
Algorithm:

Function: coustruct circle with r=n

'''
def ConstCir(radius):
    '''
    :param radius:radius of circle
    :return: matrix with circle
    Constructing matrix with a circle of radius filled with 0 surrounded with 1s. We will use this mask later to check if we have emppty space in example
    '''
    res=[]
    for i in range(radius*2+1):res.append([1]*(radius*2+1))
    #print(res)
    #radius-=1
    x0=radius
    y0=radius
    side = int(radius * math.sqrt(2))-1
    for i in range(side):
        for j in range(side):
            res[x0-side//2+i][x0-side//2+j]=0
    res[y0][x0]=0
    res[y0 + radius][x0]=0
    res[y0 - radius][x0]=0
    res[y0][x0+radius]=0
    res[y0][x0 - radius] = 0
    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius
    x = 0
    y = radius

    #for row in res:
    #    print(row)
    while (x < y) and (radius>1):
        if f >= 0:
            y -= 1
            ddf_y += 2
            f += ddf_y
        x += 1
        ddf_x += 2
        f += ddf_x
        for i in range(x0 - x,x0 + x+1):
            res[i][y0 + y-1] = 0
            res[i][y0 - y +1] = 0

        for i in range(y0 - x,y0 + x+1):
            res[x0 + y-1][i]=0
            res[x0 - y+1][i] = 0


    return (res)  # return matrix [x x]


def IsInMatr(mat1,mat2):
    '''
    :param mat1: mat1<=mat2. Mat 1 is pattert we looking for
    :param mat2: we looking in mat2. mat1 same dim as mat2. mat1 and mat2 is n x n matrix
    :return: True if found
    '''
    failflag=False
    if len(mat2[0])<3:return(False)
    for i in range(len(mat1[0])):
        for j in range(len(mat1[0])):
            if mat1[i][j]==0:
                if mat2[i][j]!=0:
                    failflag=True
                    break

    return(not(failflag))#

def printmat(z):
    '''
    Internal testing - print matrix separated by \n
    :param z:
    :return:
    '''
    for row in z:
       print(row)

maxfound=0
if n%2==0: maxlen=n//2-1
else: maxlen=n//2
#Circle cannon be bigger than n
for i in range(maxlen,0,-1):
    #Here we cut a piece of example and compare it with mask - can we build it? We going to decrease size of circle we looking for
    #until we found one. If we will not we output 0.
    example = ConstCir(i)
    if IsInMatr(example,mtrx): maxfound=i;break
    for k in range(0,n-len(example[0])):
        for l in range(0,n-len(example[0])):
            testm=[]
            for z in range(k,k+len(example[0])):
                testm.append(mtrx[z][l:l+len(example[0])])
            if IsInMatr(example, testm):
                if maxfound<i:
                 maxfound = i;
                break
print(maxfound)
f.close()