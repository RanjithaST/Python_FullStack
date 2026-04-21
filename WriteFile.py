class WriteFile:
    def writeContent(self):
        file=open("learn.txt","w")#r used means unsupported opeartion
        '''
        with open("learn.txt","r") as file:
            print(file.read())

         File "d:\Python\WriteFile.py", line 6, in writeContent
    file.write("Hi everyone")#overrides all the content present in learn.txt and replaces it with current content
    ^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: I/O operation on closed file.
 '''
        file.write("Hi everyone")#overrides all the content present in learn.txt and replaces it with current content
        #without this it wont give error but recomended bcz pipline of the file will be opened and anyone can write it
        with open("learn.txt","r") as file: #2nd way of opening file
            print(file.read()) #Hi everyone
r=WriteFile()
r.writeContent()