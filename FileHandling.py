# class FileHandling:
#     def readFile(self):
#         file=open("file1.txt","r")
#         print(file.read())
#         file.close()
#     def writeFile(self):
#         file=open("file1.txt","w")
#         file.write("Hi everyone")
#         file.close()
#         self.readFile()
# f=FileHandling()
# f.readFile()
# f.writeFile()

class FileHandling:
    def readFile(self):
        try:
            file=open("File121.txt","r")
            print(file.read())
        except FileNotFoundError as e:
            print("File not found to read")
        finally:
            try:
                file.close()
            except UnboundLocalError as e:
                print("File not found to close",str(e))
    def writeFile(self):
        try:
            file=open("File12.txt","w")
            file.write("Hello11")
        except Exception as e:
            print("Error while writing to file",e.args)
        finally:
            try:
                file.close()
            except Exception as e:
                print("Error in closing the file",str(e))
f=FileHandling()
f.readFile()
f.writeFile()
f.readFile()

'''
class FileHandling:
    def readFile(self):
    file=Nonr
        try:
            file=open("File12.txt","r")
            print(file.read())
        except FileNotFoundError as e:
            print("File not found to read",e.args)
        finally:
            if file:
                file.close()
    def writeFile(self):
        try:
            file=open("File12.txt","w")
            file.write("Hello11")
        except Exception as e:
            print("Error while writing to file",e.args)
        finally:
            if file:
                file.close()
f=FileHandling()
f.readFile()
f.writeFile()
f.readFile()
'''