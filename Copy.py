class ReadFile:
    def readContent(self):
        file=open("a.txt","r")
        s=file.read()
        file.close()
        file=open("b.txt","w")
        file.write(s)
        file.close()
r=ReadFile()
r.readContent()