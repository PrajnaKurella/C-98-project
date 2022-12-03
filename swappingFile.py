#defining a function, file1/file2 are variables which are being used for the two input values
def swappingFile():
    file1 = input("Enter the file name: ")
    file2 = input("Enter the other file: ")

#'r' is to read the file, we are saying in (whatever is file1/file2, read)
#we are using with open which is simply way to open a file and read it
    with open(file1, 'r') as da: 
        data_a = da.read()
    with open(file2, 'r') as db: 
        data_b = db.read()
    
    #'w' is for write and have a.write(data_b) is swtiching the contents of file1 into file b, same thing for b.write(data.a)
    with open(file1, 'w') as da: 
        da.write(data_b)
    with open(file2, 'w') as db: 
        db.write(data_a)
#calling the function
swappingFile()