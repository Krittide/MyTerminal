import shutil
import time
import random
import string
print("Hello user!")
print("Type 'help' for a list of commands.")
while True:
    cmd = input("MyTerminal > ")

    if cmd == "passgen": # This command will generate a random password of a specified length
        length = int(input("Enter password length: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        print("Generated password: " + password)
    elif cmd == "time": # This command will display the current time
        print("Current time is: " + time.ctime())
    elif cmd == "calc": # This command will perform basic calculations
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        if operation == "+":
            print("Sum: " + str(a + b))
        elif operation == "-":
            print("Difference: " + str(a - b))
        elif operation == "*":
            print("Product: " + str(a * b))
        elif operation == "/":
            print("Quotient: " + str(a / b))
    elif cmd == "help": # This command will display the available commands to the user
        print("Available commands: passgen, time, calc, help, clear, note, read, sysinfo, diskspace, network,hostname, uptime, ls, about,coin,guess exit")
    elif cmd == "clear": # This command will clear the terminal screen
        print("\033c", end="")
    elif cmd == "note": # This command will allow the user to write a note and save it to a file called notes.txt
        text = input("Write your note: ")
        file = open("notes.txt", "a")
        file.write(text + "\n")
        file.close()
        print("Note saved.")
    elif cmd == "read": # This command will read and display the notes from the notes.txt file
        try:
            file = open("notes.txt", "r")
            print("Your notes:")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No notes found.")
    elif cmd == "sysinfo": # This command will display system information
        import platform
        print("System: " + platform.system())
        print("Node Name: " + platform.node())
        print("Release: " + platform.release())
        print("Version: " + platform.version())
        print("Machine: " + platform.machine())
        print("Processor: " + (platform.processor() or "Unknown"))
    elif cmd == "diskspace": # This command will display the available disk space        import shutil
        total, used, free = shutil.disk_usage("/")
        print(f"Total: {total // (2**30)} GB")
        print(f"Used: {used // (2**30)} GB")
        print(f"Free: {free // (2**30)} GB")
    elif cmd == "network": # This command will display the current network configuration
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
    elif cmd == "hostname": # This command will display the system hostname
        import socket
        print("Hostname: " + socket.gethostname())
    elif cmd == "uptime": # This command will display the system uptime
        import os
        os.system("uptime")
    elif cmd == "ls": # This command will list the files in the current directory
        import os
        os.system("ls")
    elif cmd == "about": # This command will display information about the terminal
        print("MyTerminal v1.0 - A simple command-line interface written in Python.")
    elif cmd == "coin": # This command will simulate a coin flip
        result = random.choice(["Heads", "Tails"])
        print("You flipped: " + result)
    elif cmd == "guess": # This command will allow the user to play a number guessing game
        number = random.randint(1, 100)
        attempts = 0
        print("Guess a number between 1 and 100.")
        while True:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                break
    elif cmd == "exit":
        print("Goodbye!")
        break
    else:
        print("Unknown command: " + cmd)
