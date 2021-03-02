#program to predict the extension of a given filename from user.

filename = input("Input the Filename: ")
file_extn = filename.split(".")
print ("The extension of the file is: " + repr(file_extn[-1]))