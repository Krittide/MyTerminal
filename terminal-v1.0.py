import time
import random
import string
print("Hello user!")
print("Type 'help' for a list of commands.")
while True:
    cmd = input("MyTerminal > ")

    if cmd == "passgen":
        length = int(input("Enter password length: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        print("Generated password: " + password)
    elif cmd == "time":
        print("Current time is: " + time.ctime())
    elif cmd == "calc":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Sum: " + str(a + b))
    elif cmd == "help":
        print("Available commands: passgen, time, calc, help, clear, note, read, systeminfo, uptime, ls, about, exit")
    elif cmd == "clear":
        print("\033c", end="")
    elif cmd == "note":
        text = input("Write your note: ")
        file = open("notes.txt", "a")
        file.write(text + "\n")
        file.close()
        print("Note saved.")
    elif cmd == "read":
        try:
            file = open("notes.txt", "r")
            print("Your notes:")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No notes found.")
    elif cmd == "systeminfo":
        import platform
        print("System: " + platform.system())
        print("Node Name: " + platform.node())
        print("Release: " + platform.release())
        print("Version: " + platform.version())
        print("Machine: " + platform.machine())
        print("Processor: " + (platform.processor() or "Unknown"))
    elif cmd == "uptime":
        import os
        os.system("uptime")
    elif cmd == "ls":
        import os
        os.system("ls")
    elif cmd == "about":
        print("MyTerminal v1.0 - A simple command-line interface written in Python.")
    elif cmd == "exit":
        print("Goodbye!")
        break
    else:
        print("Unknown command: " + cmd)
