'''
#  0 1 2 =>stored in dynamic array(growable and shrinkable)
x=[1,2,3,1,None,None]
#0 based indexing
print(x[0])
x.append(4)
print(x)

y=list()
print(y)#[] not address
y.append(5)

a=[1,2,3,4,5]
for i in a:
    print(i)
for i in range(len(a)):
    print("***Index***")
    print(i)
    print("****Value****")
    print(a[i])
    '''
studentList=[[101,"John",85],[102,"Jane",92],[103,"Doe",78]]
for student in studentList:
    print(student)
    print(student[1])#Doe
    print(student[1][1])#o
   
    
x=[1,2,3,4,5]
print(x[-1:-6:-1])#[5, 4, 3, 2, 1] Step is always incremental so we need to mention -1 to come left
print(x[:])#[1, 2, 3, 4, 5]
print(x[::])#[1, 2, 3, 4, 5]
print(x[:6])#[1, 2, 3, 4, 5]
print(x[1:])#[2, 3, 4, 5]

#i++ not supported -> zen python
'''
while True ->infinite loop
no increment -> infinite loop
'''
a=[1,2,3,4,5]
i=0
while(i<len(a)):
    print(a[i])
    i=i+1 #without this infinite loop
'''
1
2
3
4
5
'''