# MyTerminal

A simple command-line interface simulator written in Python.

## Description

This script mimics a basic terminal with various commands. It provides a interactive prompt where users can enter commands to perform different actions.

## How to Run

1. Ensure you have Python installed on your system.
2. Run the script using: `python terminal-V1.0.py`

## Available Commands

- `hello`: Prints a greeting message.
- `time`: Displays the current time.
- `calc`: Performs addition of two numbers entered by the user.
- `help`: Lists all available commands.
- `clear`: Clears the terminal screen.
- `note`: Allows writing a note to a file (notes.txt).
- `read`: Reads and displays saved notes from notes.txt.
- `systeminfo`: Shows system information.
- `exit`: Exits the terminal simulator.

## Usage

When you run the script, it will display: "Type 'help' for a list of commands."

Then, enter commands at the "MyTerminal > " prompt.

For example:
- Type `hello` and press Enter to see "Hello user!"
- Type `time` to see the current time.
- Type `calc` to add two numbers.
- Type `exit` to quit.

## Notes

- The `note` command appends to notes.txt in the same directory.
- The `read` command reads from notes.txt.
- System info uses the `platform` module.

## Requirements

- Python 3.x
- No external dependencies required.