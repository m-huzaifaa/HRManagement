import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self, name, address, phone_number, salary):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.salary = salary

class HRSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, address, phone_number, salary):
        employee = Employee(name, address, phone_number, salary)
        self.employees.append(employee)
        messagebox.showinfo("Success", f"Employee {name} added successfully.")

    def calculate_salary(self, employee_name):
        for emp in self.employees:
            if emp.name == employee_name:
                messagebox.showinfo("Salary", f"Salary of {emp.name}: ${emp.salary}")
                return
        messagebox.showerror("Error", f"Employee with name {employee_name} not found.")

    def view_employees(self):
        employee_list = "\n".join([emp.name for emp in self.employees])
        messagebox.showinfo("Employees", f"Employees:\n{employee_list}")

    def update_employee(self, name, new_address, new_phone_number, new_salary):
        for emp in self.employees:
            if emp.name == name:
                emp.address = new_address
                emp.phone_number = new_phone_number
                emp.salary = new_salary
                messagebox.showinfo("Success", f"Employee {name} updated successfully.")
                return
        messagebox.showerror("Error", f"Employee with name {name} not found.")

    def delete_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                messagebox.showinfo("Success", f"Employee {name} deleted successfully.")
                return
        messagebox.showerror("Error", f"Employee with name {name} not found.")

def add_employee_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Employee")

    # Labels and Entry widgets for employee details
    tk.Label(add_window, text="Name:").grid(row=0, column=0)
    tk.Label(add_window, text="Address:").grid(row=1, column=0)
    tk.Label(add_window, text="Phone Number:").grid(row=2, column=0)
    tk.Label(add_window, text="Salary:").grid(row=3, column=0)

    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1)
    address_entry = tk.Entry(add_window)
    address_entry.grid(row=1, column=1)
    phone_entry = tk.Entry(add_window)
    phone_entry.grid(row=2, column=1)
    salary_entry = tk.Entry(add_window)
    salary_entry.grid(row=3, column=1)

    def add_employee():
        name = name_entry.get()
        address = address_entry.get()
        phone_number = phone_entry.get()
        salary = float(salary_entry.get())
        hr_system.add_employee(name, address, phone_number, salary)
        add_window.destroy()

    tk.Button(add_window, text="Add Employee", command=add_employee).grid(row=4, column=0, columnspan=2)

def view_employees():
    hr_system.view_employees()

def update_employee_window():
    update_window = tk.Toplevel(root)
    update_window.title("Update Employee")

    tk.Label(update_window, text="Employee Name:").grid(row=0, column=0)
    tk.Label(update_window, text="New Address:").grid(row=1, column=0)
    tk.Label(update_window, text="New Phone Number:").grid(row=2, column=0)
    tk.Label(update_window, text="New Salary:").grid(row=3, column=0)

    name_entry = tk.Entry(update_window)
    name_entry.grid(row=0, column=1)
    new_address_entry = tk.Entry(update_window)
    new_address_entry.grid(row=1, column=1)
    new_phone_entry = tk.Entry(update_window)
    new_phone_entry.grid(row=2, column=1)
    new_salary_entry = tk.Entry(update_window)
    new_salary_entry.grid(row=3, column=1)

    def update_employee():
        name = name_entry.get()
        new_address = new_address_entry.get()
        new_phone_number = new_phone_entry.get()
        new_salary = float(new_salary_entry.get())
        hr_system.update_employee(name, new_address, new_phone_number, new_salary)
        update_window.destroy()

    tk.Button(update_window, text="Update Employee", command=update_employee).grid(row=4, column=0, columnspan=2)

def delete_employee_window():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Employee")

    tk.Label(delete_window, text="Employee Name:").grid(row=0, column=0)
    name_entry = tk.Entry(delete_window)
    name_entry.grid(row=0, column=1)

    def delete_employee():
        name = name_entry.get()
        hr_system.delete_employee(name)
        delete_window.destroy()

    tk.Button(delete_window, text="Delete Employee", command=delete_employee).grid(row=1, column=0, columnspan=2)

root = tk.Tk()
root.title("HR System")

hr_system = HRSystem()

add_button = tk.Button(root, text="Add Employee", command=add_employee_window)
add_button.pack()

view_button = tk.Button(root, text="View Employees", command=view_employees)
view_button.pack()

update_button = tk.Button(root, text="Update Employee", command=update_employee_window)
update_button.pack()

delete_button = tk.Button(root, text="Delete Employee", command=delete_employee_window)
delete_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()
