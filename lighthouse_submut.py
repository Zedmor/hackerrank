#!/usr/bin/python
import math

#f = open("lighthouse.txt","r")
n=int(input())

pic=[]
mtrx=[]
for i in range(n):
    mtrx.append(input())

for i in range(n):
     mtrx[i]=mtrx[i].replace(".","0");mtrx[i]=mtrx[i].replace("*","1")
     mtrx[i]=list(map(int,mtrx[i]))

mtrx=mtrx[:n]

maxfound=0
'''
Algorithm:

Function: coustruct circle with r=n

'''
def ConstCir(radius):
    '''
    :param radius:radius of circle
    :return: matrix with circle
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
    #for row in res:
    #    print(row)
    res[y0][x0]=0
    res[y0 + radius][x0]=0
    res[y0 - radius][x0]=0
    res[y0][x0+radius]=0
    res[y0][x0 - radius] = 0
    #if radius%2!=0: radius-=1
    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius
    x = 0
    y = radius

    #for row in res:
    #    print(row)
    while x < y:
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

# Bitmap.circle = circle
#
# bitmap = Bitmap(25, 25)
# bitmap.circle(x0=12, y0=12, radius=12)
# bitmap.chardisplay()


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
    for row in z:
       print(row)
if n%2==0: maxlen=n//2-1
else: maxlen=n//2
for i in range(maxlen,0,-1):
    example = ConstCir(i)
    # print(i)

    if IsInMatr(example,mtrx): maxfound=i;break
    # print(len(example[0]))
    for k in range(0,n-len(example[0])):
        for l in range(0,n-len(example[0])):
            #found=FitBitmap(example,
            testm=[]
            for z in range(k,k+len(example[0])):
                testm.append(mtrx[z][l:l+len(example[0])])
            #printmat(example);printmat(testm)
            if IsInMatr(example, testm):
                if maxfound<i: maxfound = i
                # printmat(example)
                # printmat(testm);print('');
                break
    #         for row in testm:
    #            print(row)
    #         print('')
    # print('')
    #Construct circle with i radius
    #Find circle c in matrix mtrx
    #if true: maxfound=i;break

print(maxfound)

#f.close()