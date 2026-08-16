
from . import oops_intro as oops
from .exercise import vehicle_rental as vr

def __oops_practice():
    try:
        vr.Vehicle("Skeleton Vehicle")
    except TypeError:
        print("Abstract classes shouldn't be initiated")

    mazda = vr.Car("Mazda 3", 4, 220, 90)
    print(f"{mazda.brand} speed / battery_level is clamped to {mazda.speed} and {mazda.battery_level}")
    
    bike = vr.Bike("Royal Enfield", True, 180, 80)

    for vehicle in [mazda, bike]:
        print(vehicle.describe())

    print(f"Total vehicles in the rental so far: {vr.Vehicle.total_vehicles}")
    

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
    __oops_practice()