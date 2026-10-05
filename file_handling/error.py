try:
    with open("notesss.txt","r")as file:
        data=file.read()
except FileNotFoundError:
    print("sorry this file is does'nt exist")
            