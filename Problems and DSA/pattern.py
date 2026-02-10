#Nested loops
#outer loop for rows(lines) 
#inner loop for columns and connect them somehow to the rows
#print pattern inside the inner loop
#observe symmetry(optional)

'''
Docstring for Problems and DSA.pattern
**** 0->4 stars
**** 1->4
**** 2->4
**** 3->4
'''
def printPatter1(N):
    for i in range(0,N):
        for j in range(0,N):
            print("*",end=" ")
        print(" ")
printPatter1(4)
print(" ")

'''
Docstring for Problems and DSA.pattern
*       0->1 stars
**      1->2
***     2->3
****    3->4
'''
def printPatter2(N):
    for i in range(0,N):
        for j in range(0,i):
            print("*",end=" ")
        print(" ")
printPatter2(4)

'''
Docstring for Problems and DSA.pattern
1       0->1 stars
12      1->2
123     2->3
1234    3->4
'''
def printPatter3(N):
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print(" ")
printPatter3(4)

'''
Docstring for Problems and DSA.pattern
1       0->1 stars
12      1->2
123     2->3
1234    3->4
'''
def printPatter3(N):
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print(" ")
printPatter3(4)

'''
Docstring for Problems and DSA.pattern
1       0->1 stars
22      1->2
333     2->3
4444    3->4
'''
def printPatter4(N):
    for i in range(1,N+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print(" ")
printPatter4(4)







