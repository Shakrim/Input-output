"""
Python Homework Assignment #8: Input and Output (I/O)
Details:
Create a note-taking program. When a user starts it up, it should prompt them for a filename.
If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.
If they enter a file name that already exists, it should ask the user if they want:
A) Read the file
B) Delete the file and start over
C) Append the file
If the user wants to read the file it should simply show the contents of the file on the screen.
If the user wants to start over then the file should be deleted and another empty one made in its place.
If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file.
Extra Credit:
Allow the user to select a 4th option:
D) Replace a single line
If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:
1) The line number they want to update.
2) The text that should replace that line.
"""
#creating of note-taking program

import os.path
Note_taking_file = input("Enter the filename: ")
# check if the file exists
if os.path.isfile(Note_taking_file):
    while True:
        action = input("Please select what to do with the file (<read>,<write>,<append>,<writeline>) or <done> for stop: " )
        if action == "read":
            f = open(Note_taking_file, "r")
            content = f.read()
            print(content)
            f.close()

        elif action == "write":
            f = open(Note_taking_file, "w")
            f.write(input("You are in re-writing mode: "))
            f.close()

        elif action == "append":
            f = open(Note_taking_file, "a")
            f.write(input("You are in writing mode: "))
            f.close()

        elif action == "writeline":
            number_line = int(input("Please select the line number you want to update: "))
            text_into_line = input("You are in writing mode: ")
            f = open(Note_taking_file, "r")
            lines = f.readlines()
            lines[number_line] = text_into_line
            f.close()
            f = open(Note_taking_file, "w")
            f.writelines(lines)
            f.close()
        elif action == "done":
            break
        elif action != "read" or action != "write" or action != "append" or action != "writeline":
            print("Error action.")

else:
    print(f'This file {Note_taking_file} does not exist. Creating the file {Note_taking_file}')
    f = open(Note_taking_file, "w")
    f.write(input("You are in writing mode: "))
    f.close()
