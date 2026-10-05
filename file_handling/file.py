file=open("C:\\Users\\muham\\OneDrive\\Desktop\\Hoja python practical\\file_handling\\notes.txt","r")
for line in file:
    print(line.strip())
file.close()
