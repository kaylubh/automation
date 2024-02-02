from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table

import os
import shutil


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


def parse_directory_logs(user):
    """
    
    """

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
            user = Prompt.ask("\nEnter name of the user directory")
            archive_directory(user)
        elif menu_selection == "4":
            sort_directory()
        elif menu_selection == "5":
            parse_directory_logs()
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
