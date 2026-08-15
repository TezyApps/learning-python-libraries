
from . import oops_intro as oops

def __manager_example():
    manager = {'name': 'John Doe', 'role': 'manager', 'password': 'admin', 'tasks': []}
    office_manager = oops.Office(manager)
    office_manager.login('admin')
    office_manager.add_task('verify tasks')
    office_manager.add_task('cancel schedule')
    office_manager.add_task('do 1:1')
    manager_tasks = office_manager.view_tasks()
    # print(office_manager.__user_data) # AttributeError: 'Office' object has no attribute '__user_data'
    print(manager_tasks)

def __employee_example():
    employee = {'name': 'Jane Doe', 'role': 'employee', 'password': 'user', 'tasks': []}

    office_employee = oops.Office(employee)
    office_employee.login('user')
    office_employee.add_task('verify tasks')
    office_employee.add_task('cancel schedule')
    office_employee.add_task('do 1:1')
    employee_tasks = office_employee.view_tasks()
    print(employee_tasks)

def main() -> None:
    print("Welcome to OOPS in Python!")
    __manager_example()
    __employee_example()