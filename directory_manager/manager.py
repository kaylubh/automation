from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table

import os
import shutil
import re


console = Console()

user_directory_root = "user_directory"

def view_directory(user):
    """
    
    """

    try:
        user_path = os.path.join(user_directory_root, user)
        files = os.listdir(user_path)

        table = Table(title=f"\n{user} Directory")
        table.add_column("File Names", style="dim")
        for file in files:
            table.add_row(file)
        
        console.print(table)

    except FileNotFoundError:
        console.print(f"\n[bold red]No directory found for {user}[/bold red]")

def make_directory(user):
    """
    
    """

    confirmation = Confirm.ask(f"\nAre you sure you want to create a new directory for {user}?")

    if confirmation:

        try:
            user_path = os.path.join(user_directory_root, user)

            os.mkdir(user_path)
            
            console.print(f"\nDirectory created for {user}")

        except FileNotFoundError:
            console.print(f"\n[bold red]No directory found for {user}[/bold red]")

    else:

        console.print("\n[bold red]Task Cancelled[/bold red]")

def archive_directory(user):
    """
    
    """

    confirmation = Confirm.ask(f"\nAre you sure you want to archive the directory for {user}?")

    if confirmation:

        try:
            user_path = os.path.join(user_directory_root, user)
            archive_path = os.path.join(user_directory_root, "archive", user)

            shutil.move(user_path, archive_path)
            
            console.print(f"\nDirectory for {user} archived")

        except FileNotFoundError:
            console.print(f"\n[bold red]No directory found for {user}[/bold red]")

    else:

        console.print("\n[bold red]Task Cancelled[/bold red]")

def sort_directory(user):
    """
    
    """

    confirmation = Confirm.ask(f"\nAre you sure you want to sort the directory for {user}?")

    if confirmation:

        try:
            user_path = os.path.join(user_directory_root, user)
            files = os.listdir(user_path)

            for file in files:

                if re.search(r"\.mail$", file):
                    mail_dir = os.path.join(user_path, "mail")
                    os.makedirs(mail_dir, exist_ok=True)
                    unsorted_path = os.path.join(user_path, file)
                    sorted_path = os.path.join(mail_dir, file)
                    shutil.move(unsorted_path, sorted_path)

                if re.search(r"\.log\.txt$", file):
                    logs_dir = os.path.join(user_path, "logs")
                    os.makedirs(logs_dir, exist_ok=True)
                    unsorted_path = os.path.join(user_path, file)
                    sorted_path = os.path.join(logs_dir, file)
                    shutil.move(unsorted_path, sorted_path)
                
            console.print(f"\n[bold green]Directory sorted for {user}[/bold green]")

        except FileNotFoundError:
            console.print(f"\n[bold red]No directory found for {user}[/bold red]")

    else:

        console.print("\n[bold red]Task Cancelled[/bold red]")

def parse_directory_logs(user):
    """
    
    """

    confirmation = Confirm.ask(f"\nAre you sure you want to parse the logs for {user}?")

    if confirmation:

        try:
            user_logs_path = os.path.join(user_directory_root, user, "logs")
            log_files = os.listdir(user_logs_path)

            errors_logs = []
            warnings_logs = []

            for log_file in log_files:

                if re.search(r"\.log\.txt$", log_file):
                    log_file_path = os.path.join(user_logs_path, log_file)
                    with open(log_file_path, "r") as file:
                        lines = file.readlines()
                        errors_logs += [line for line in lines if re.search(r"ERROR:", line)]
                        warnings_logs += [line for line in lines if re.search(r"WARNING:", line)]

            errors_log_file_path = os.path.join(user_logs_path, "errors.log")
            warnings_log_file_path = os.path.join(user_logs_path, "warnings.log")

            with open(errors_log_file_path, "w") as file:
                file.writelines(errors_logs)

            with open(warnings_log_file_path, "w") as file:
                file.writelines(warnings_logs)

            console.print(f"\n[bold green]Directory logs for {user} parsed[/bold green]")

        except FileNotFoundError:
            console.print(f"\n[bold red]No logs found for {user}[/bold red]")
            console.print(f"[bold red]If a directory exists for {user}, ensure the directory has been sorted[/bold red]")

    else:

        console.print("\n[bold red]Task Cancelled[/bold red]")


def backup_directory(user):
    """
    
    """


def main():
    """
    
    """

    console.print("\n*** Welcome to the User Directory Management Tool ***")

    while True:

        console.print("\n1. View User Directory\n2. Create New User Directory\n3. Archive User Directory\n4. Sort User Directory\n5. Parse User Directory Logs\n6. Backup User Directory\n7. Exit Tool\n")

        menu_selection = Prompt.ask("Choose a task to execute (User number in above list)", choices=["1", "2", "3", "4", "5", "6", "7"], default="7")

        if menu_selection == "1":
            user = Prompt.ask("\nEnter name of the user directory")
            view_directory(user)
        elif menu_selection == "2":
            user = Prompt.ask("\nEnter name of the user to create directory")
            make_directory(user)
        elif menu_selection == "3":
            user = Prompt.ask("\nEnter name of the user directory to archive")
            archive_directory(user)
        elif menu_selection == "4":
            user = Prompt.ask("\nEnter name of the user directory to sort")
            sort_directory(user)
        elif menu_selection == "5":
            user = Prompt.ask("\nEnter name of the user directory to parse logs")
            parse_directory_logs(user)
        elif menu_selection == "6":
            backup_directory()
        elif menu_selection == "7":
            break

    console.print("\n*** Exiting the User Directory Management Tool ***\n")

###############
## Start App ##
###############
    
if __name__ == "__main__":
    main()
