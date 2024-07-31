def read_file():
    fp = open("file1.txt","r")
    for i in fp.read():
        print(i)
    fp.close()

def write_file(strs):
    fp = open("file1.txt","w")
    fp.write(strs)
    fp.close()

def append_file(strs1):
    fp = open("file1.txt","a")
    fp.write(strs1)
    fp.close()
