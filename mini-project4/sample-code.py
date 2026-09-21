# File-Based Notes App
note = input("Enter your note: ")
file = open("notes.txt", "a")
file.write(note + "\n")
file.write(note + "\n")
file.write(note + "\n")

file.close()
print("Note saved successfully!")
# Read notes
file = open("notes.txt", "r")
print("\n====== SAVED NOTES ======")
print(file.read())
file.close()