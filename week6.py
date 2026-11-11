print("Hello World")
#opening a file
File_object = open(r"MyFile1.txt")

# Open function to open the file "MyFile1.txt" # (same directory) in append mode and

file1 = open("MyFile1.txt","a")

# store its reference in the variable file1

# and "MyFile2.txt" in D:\Text in file2 file2 = open(r"D:\Text\MyFile2.txt","w+")


#Closing a file
# Opening and Closing a file "MyFile.txt" # for object name file1.
file1 = open("MyFile.txt","a")
file1.close()

#Industry standard practice.
with open("MyFile1.txt", "r") as f:
    data = f.read()
    print(data)

#Writing to a file
#There are two ways to write in a file.
#write() : Inserts the string str1 in a single line in the text file
#File_object.write(str1), File_object.writelines(L) for L = [str1, str2, str3]


#Reading from a file
#read() : File_object.read([n])
#readline() : File_object.readline([n])
#readlines() : File_object.readlines([n])


# Program to show various ways to read and # write data in a file.
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]


# \n is placed to indicate EOL (End of Line) file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes


file1 = open("myfile.txt","r+")


print("Output of Read function is ")
print(file1.read())
print()


# byte from the beginning.
file1.seek(0)


print( "Output of Readline function is ")
print(file1.readline())
print()


file1.seek(0)
# To show difference between read and readline print("Output of Read(9) function is ") print(file1.read(9))
print()
file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()


#Appending to a file
# Python program to illustrate # Append vs write mode
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.writelines(L)
file1.close()


# Append-adds at last
file1 = open("myfile.txt","a")#append mode file1.write("Today \n")
file1.close()


file1 = open("myfile.txt","r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt","w") #write mode file1.write("Tomorrow \n")
file1.close()


file1 = open("myfile.txt","r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()


import pandas as pd
df = pd.read_csv("data(2).csv")
print(df)

#Write an Excel File
df.to_excel('data(2).xlsx')

#JSON Files
df.to_json('data-columns.json')




# seek(n) takes the file handle to the nth



