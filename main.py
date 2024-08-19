class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Your task '{task}' added")
    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            deleted_task = self.tasks.pop(task_number)
            print(f"Your task '{deleted_task}' deleted")
        else:
            print("Invalid task number")
    def show_tasks(self):
        if not self.tasks:
            print("There are no tasks")
        else:
            print("Your tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

class LoginPassword:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def register_user(self, username, password):
        if username in self.users:
            print("This username already exists")
        else:
            self.users[username] = password
            print("User registered")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.current_user = username
            print("User logged in")
        else:
            print("Invalid username or password")

    def logout(self):
        if self.current_user:
            print("User logged out")
            self.current_user = None
        else:
            print("You are not logged in")


def print_help():
    print("""
    Functions:
    register <username> <password> -- Register a new user
    login <username> <password>    -- Login with an existing user
    logout                         -- Logout the current user
    add <task>                     -- Add a new task
    delete <number>                -- Delete a task
    show                           -- Show all tasks
    help                           -- Show this message
    exit                           -- Exit the program
    """)


def main():
    login_password = LoginPassword()
    todo_list = {}
    print("Welcome to TodoList")
    print_help()
    while True:
        command = input("\nEnter your command: ").strip().lower()
        parts = command.split()
        if not parts:
            continue
        action = parts[0]
        args = parts[1:]

        if action == "register":
            if len(args) == 2:
                username, password = args
                login_password.register_user(username, password)
            else:
                print("Usage: register <username> <password>")
        elif action == "login":
            if len(args) == 2:
                username, password = args
                login_password.login(username, password)
                if login_password.current_user and login_password.current_user not in todo_list:
                    todo_list[login_password.current_user] = TodoList()
            else:
                print("Usage: login <username> <password>")
        elif action == "logout":
            login_password.logout()
        elif action == "add":
            if login_password.current_user:
                task = " ".join(args)
                if task:
                    todo_list[login_password.current_user].add_task(task)
                else:
                    print("Enter your task")
            else:
                print("You need to be logged in to add tasks")
        elif action == "delete":
            if login_password.current_user:
                try:
                    task_number = int(args[0]) - 1
                    todo_list[login_password.current_user].delete_task(task_number)
                except (IndexError, ValueError):
                    print("Please enter a valid task number")
            else:
                print("You need to be logged in to delete tasks")
        elif action == "show":
            if login_password.current_user:
                todo_list[login_password.current_user].show_tasks()
            else:
                print("You need to be logged in to show tasks")
        elif action == "help":
            print_help()
        elif action == "exit":
            print("Thank you for using TodoList")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands")


if __name__ == "__main__":
    main()

