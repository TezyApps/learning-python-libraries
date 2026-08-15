
class Office:

    @property
    def __name(self) -> str:
        return self.__user_data['name']

    def __init__(self, user_data: dict):
        self.__user_data = user_data

    def login(self, password: str):
        if self.__user_data['password'] == password:
            print(f"Logged In. Welcome back {self.__name}!")
        else:
            print(f"Unable to login. Please try again.")

    def view_tasks(self) -> list:
        return self.__user_data['tasks']

    def add_task(self, task: str) -> None:
        if self.__user_data['role'] == 'manager':
            self.__user_data['tasks'].append(task)
            print("Task added successfully")
        else:
            print('You don\'t have necessary permission to add a task.')