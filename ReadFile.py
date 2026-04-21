class ReadFile:
    def readContent(self):
        file=open("learn.txt","r")
        
        #print(file.read())#read all the content at 1 shot
        '''
        I am attending Python sessions
        I am learning SQL
        '''
        #print(file.close()) none
        print(file.readline())#I am attending Python sessions
        print(file.readline())

        '''
            I am attending Python sessions

        I am learning SQL
     '''
        file.close()#without this it wont give error but recomended bcz pipline of the file will be opened and anyone can write it
r=ReadFile()
r.readContent()