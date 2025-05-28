# Supported Commands:
#   pwd             - Show current directory
#   cd DIR          - Change directory
#   cd..            - Go up one directory
#   mkdir NAME      - Make new directory
#   ls              - List files and folders
#   touch FILE      - Create a new file
#   rmdir NAME      - Remove a directory
#   history         - Show command history
#   help            - Show this help menu
#   about           - Info about this shell
#   clear           - Clear the terminal
#   count           - Count items in current directory
#   rename OLD NEW  - Rename a file or folder
#   exit            - Exit the shell

import os
import sys
import subprocess

if os.name == 'nt':
    os.system('')  # Enables ANSI escape codes in terminal (Windows 10+)


# ANSI color codes for styling
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

history = []  # Store command history

def execute_command(command):
    command = command.strip()
    if not command:
        return

    history.append(command)  # Save to history
    parts = command.split()
    cmd = parts[0]
    args = parts[1:]

    # exit
    if cmd == "exit":
        print(f"{GREEN}Goodbye from PentaShell!{RESET}")
        sys.exit(0)

    # pwd
    elif cmd == "pwd":
        print(os.getcwd())

    #cd
    elif cmd == "cd":
      if args:
        target_dir = " ".join(args)  # Handles folder names with spaces
        if os.path.isabs(target_dir):
            new_path = target_dir
        else:
            new_path = os.path.join(os.getcwd(), target_dir)

        if os.path.isdir(new_path):
            os.chdir(new_path)
        else:
            print(f"cd error: Directory not found -> {target_dir}")
      else:
        print("cd: missing argument")

    
    #cd..
    elif cmd == "cd..":
        try:
          os.chdir("..")
        except Exception as e:
          print(f"cd error: {e}")


    # mkdir
    elif cmd == "mkdir":
        for directory in args:
            try:
                os.mkdir(directory)
                print(f"{GREEN}Directory '{directory}' created.{RESET}")
            except Exception as e:
                print(f"{RED}mkdir error: {e}{RESET}")

    # ls
    elif cmd == "ls":
        print("\n".join(os.listdir()))

    # touch
    elif cmd == "touch":
        for filename in args:
            try:
                open(filename, 'a').close()
                print(f"{GREEN}File '{filename}' created.{RESET}")
            except Exception as e:
                print(f"{RED}touch error: {e}{RESET}")

    # rmdir
    elif cmd == "rmdir":
        for directory in args:
            try:
                os.rmdir(directory)
                print(f"{GREEN}Directory '{directory}' removed.{RESET}")
            except Exception as e:
                print(f"{RED}rmdir error: {e}{RESET}")

    # history
    elif cmd == "history":
        for idx, entry in enumerate(history):
            print(f"{idx+1}: {entry}")

    # help
    elif cmd == "help":
        print(f"""{YELLOW}
{BOLD}Supported Commands:{RESET}
  {BOLD}pwd{RESET}             - Show current directory
  {BOLD}cd DIR{RESET}          - Change directory
  {BOLD}cd..{RESET}            - Go up one directory
  {BOLD}mkdir NAME{RESET}      - Make new directory
  {BOLD}ls{RESET}              - List files and folders
  {BOLD}touch FILE{RESET}      - Create a new file
  {BOLD}rmdir NAME{RESET}      - Remove a directory
  {BOLD}history{RESET}         - Show command history
  {BOLD}clear{RESET}           - Clear the terminal
  {BOLD}rename OLD NEW{RESET}  - Rename file/folder
  {BOLD}count{RESET}           - Count items in current directory
  {BOLD}about{RESET}           - Info about this shell
  {BOLD}exit{RESET}            - Exit the shell
""")

    # about
    elif cmd == "about":
        print(f"{YELLOW}PentaShell v1.1 — Created with by Penta (Hajira, Kinza, Areeba , Fatima, Aatikah) {RESET}")

    # clear
    elif cmd == "clear":
        os.system("cls" if os.name == "nt" else "clear")

    # count
    elif cmd == "count":
        try:
            items = os.listdir()
            print(f"{GREEN}Total items: {len(items)}{RESET}")
        except Exception as e:
            print(f"{RED}count error: {e}{RESET}")

    # rename
    elif cmd == "rename":
        if len(args) != 2:
            print(f"{RED}Usage: rename old_name new_name{RESET}")
        else:
            try:
                os.rename(args[0], args[1])
                print(f"{GREEN}Renamed '{args[0]}' to '{args[1]}'{RESET}")
            except Exception as e:
                print(f"{RED}rename error: {e}{RESET}")

    # External fallback
    else:
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"{RED}Command error: {e}{RESET}")

def main():
    print(f"{RED}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx{RESET}")
    print(f"{YELLOW}         --------------------------------- Welcome to {BOLD}PentaShell{RESET}{YELLOW} ---------------------------------{RESET}")
    print(f"{RED}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx{RESET}")
    while True:
        try:
            command = input(f"{BLUE}{BOLD}PentaShell>> {RESET}")
            execute_command(command)
        except EOFError:
            break

if __name__ == "__main__":
    main()


