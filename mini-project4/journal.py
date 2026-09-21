# Journal Application
journaldate = input("enter date for journal entry: ")
print(f"today's date is {journaldate}")
journalentry = input("enter your journal entry(50-100 words): ")
file = open("journal.md", "a")
file.write(f"date: {journaldate}\n{journalentry}\n\n")
file.close()
print("Journal successfully entered and saved!!")
file = open("journal.md", "r")

print("\n********* SAVED JOURNAL ENTRY *********")
print(file.read())
file.close()
