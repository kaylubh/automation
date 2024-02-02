from rich.console import Console
from rich.prompt import Prompt


console = Console()

def view_directory(user_directory):
    """
    
    """

def make_directory(user_directory):
    """
    
    """

def archive_directory(user_directory):
    """
    
    """

def sort_directory(user_directory):
    """
    
    """

def parse_directory_logs(user_directory):
    """
    
    """

def backup_directory(user_directory):
    """
    
    """

def exit_app():
    """
    
    """

    console.print("\n*** Exiting the User Directory Management Tool ***\n")

def main():
    """
    
    """

    console.print("\n*** Welcome to the User Directory Management Tool ***")
    console.print("\n1. View User Directory\n2. Create New User Directory\n3. Archive User Directory\n4. Sort User Directory\n5. Parse User Directory Logs\n6. Backup User Directory\n7. Exit Tool\n")
    menu_selection = Prompt.ask("Choose a task to execute (User number in above list)", choices=["1", "2", "3", "4", "5", "6", "7"], default="7")

    if menu_selection == "1":
        view_directory()
    elif menu_selection == "2":
        make_directory()
    elif menu_selection == "3":
        archive_directory()
    elif menu_selection == "4":
        sort_directory()
    elif menu_selection == "5":
        parse_directory_logs()
    elif menu_selection == "6":
        backup_directory()
    elif menu_selection == "7":
        exit_app()

###############
## Start App ##
###############
    
if __name__ == "__main__":
    main()
