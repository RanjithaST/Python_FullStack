#selecion of i and j should be done for printing the star.select to print only when there is required
'''
Docstring for DSA.BoundaryPattern
*  *  *  *  *  *  *  *  *   
*                       *   
*                       *
*                       *
*                       *
*                       *
*                       *
*                       *
*  *  *  *  *  *  *  *  *
use if and else inside j loop
'''
n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==1 or i==n or j==1 or j==n):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print(" ")
'''
Normal diagonal-starts from left and goes to the right
Row no=Column no
*  *  *  *  *  *  *  *  * i==1
*  *  (1==1)            *
*     *  (2==2)         *
*        *              *
*           *           *
*              *        *
*                 *     *
*                    *  *
*  *  *  *  *  *  *  *  * i==n
j==1                    j==n
'''
n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==1 or i==n or j==1 or j==n or i==j):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print(" ")

'''
Cross diagonal-common sum diagonal:right to left
*  *  *  *  *  *  *  *  *(1,9)
*                    * (2,8) *
*                 *(3,7)   *
*              *(4,6)      *
*           *           *
*        *              *
*     *                 *
*  *                    *
*  *  *  *  *  *  *  *  *
'''
n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==1 or i==n or j==1 or j==n or i+j==n+1):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print(" ")
'''
*(i==j)                 *(i+j==n)
   *                 *
      *           *
         *     *
            *
         *     *
      *           *
   *                 *
*                       *
'''
n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==j or i+j==n+1):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print(" ")

'''
*
*  *
*     *
*        *
*           *
*              *
*                 *
*                    *
*  *  *  *  *  *  *  *  *
'''
n=9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==j or j==1 or i==n):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print(" ")