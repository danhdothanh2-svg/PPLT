# ================= DATA MANAGEMENT CLASS =================
# Parent class
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        return "Undefined"

# Child class: Full-time employee
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, base_salary):
        super().__init__(emp_id, name)
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

# Child class: Part-time employee
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, work_hours, hourly_rate):
        super().__init__(emp_id, name)
        self.work_hours = work_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.work_hours * self.hourly_rate


# ================= SYSTEM MANAGEMENT CLASS =================
class EmployeeManagementSystem:
    def __init__(self):
        self.employee_list = []

    def add_fulltime_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        base_salary = float(input("Enter Base Salary: "))
        employee = FullTimeEmployee(emp_id, name, base_salary)
        self.employee_list.append(employee)

        print("Full-time employee added successfully!")

    def add_parttime_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        work_hours = float(input("Enter Work Hours: "))
        hourly_rate = float(input("Enter Hourly Rate: "))
        employee = PartTimeEmployee(emp_id, name, work_hours, hourly_rate)
        self.employee_list.append(employee)

        print("Part-time employee added successfully!")

    def display_employees(self):
        if len(self.employee_list) == 0:
            print("No employees found.")
            return

        print("\n===== EMPLOYEE LIST =====")

        for employee in self.employee_list:
            print(f"ID: {employee.emp_id}")
            print(f"Name: {employee.name}")
            print(f"Salary: {employee.calculate_salary()}")
            print("------------------------")


# ================= LIST PROGRAM =================
system = EmployeeManagementSystem()

while True:
    print("\n===== EMPLOYEE MANAGEMENT MENU =====")
    print("1. Add Full-time Employee")
    print("2. Add Part-time Employee")
    print("3. Display Employees")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_fulltime_employee()
    elif choice == "2":
        system.add_parttime_employee()
    elif choice == "3":
        system.display_employees()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")