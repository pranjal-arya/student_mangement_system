from Teacher import Teacher
from Student import Student
from Admin import Admin

def display_main_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print(" "*15 + "SCHOOL MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Admin Login")
    print("2. Student Operations")
    print("3. Teacher Operations")
    print("4. Exit")
    print("="*60)

def display_admin_menu():
    """Display admin menu"""
    print("\n" + "-"*60)
    print(" "*20 + "ADMIN MENU")
    print("-"*60)
    print("--- Admin Profile ---")
    print("1. View Admin Profile")
    print("2. Update Admin Profile")
    print("3. Create New Admin")
    print("4. List All Admins")
    print("\n--- Student Management ---")
    print("5. Add Student")
    print("6. Remove Student")
    print("7. View All Students")
    print("8. Update Student")
    print("9. Search Student by Name")
    print("\n--- Teacher Management ---")
    print("10. Add Teacher")
    print("11. Remove Teacher")
    print("12. View All Teachers")
    print("13. Update Teacher")
    print("14. Search Teacher by Name")
    print("\n--- Reports & Analytics ---")
    print("15. Generate Class Report")
    print("16. View Top Students")
    print("17. System Statistics")
    print("18. Export Class Data")
    print("19. Bulk Delete Class Students")
    print("\n20. Logout")
    print("-"*60)

def display_student_menu():
    """Display student menu"""
    print("\n" + "-"*60)
    print(" "*18 + "STUDENT OPERATIONS")
    print("-"*60)
    print("1. Create New Student")
    print("2. View Student Details")
    print("3. Update Student Details")
    print("4. Check Student Marks")
    print("5. Update Student Marks")
    print("6. Delete Student")
    print("7. List All Students")
    print("8. Search Student by Name")
    print("9. Get Class Average")
    print("10. Back to Main Menu")
    print("-"*60)

def display_teacher_menu():
    """Display teacher menu"""
    print("\n" + "-"*60)
    print(" "*18 + "TEACHER OPERATIONS")
    print("-"*60)
    print("1. Create New Teacher")
    print("2. View Teacher Details")
    print("3. Update Teacher Details")
    print("4. Delete Teacher")
    print("5. List All Teachers")
    print("6. Back to Main Menu")
    print("-"*60)

def handle_admin_operations():
    """Handle admin login and operations"""
    print("\n--- Admin Login ---")
    admin_id = input("Enter Admin ID: ")
    password = input("Enter Password: ")
    
    admin = Admin(admin_id, password)
    
    if not admin.is_authenticated:
        print("Login failed. Returning to main menu.")
        return
    
    while True:
        display_admin_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            # View Admin Profile
            admin.read_admin()
        
        elif choice == "2":
            # Update Admin Profile
            print("\n--- Update Admin Profile ---")
            name = input("Enter new name (or press Enter to skip): ")
            email = input("Enter new email (or press Enter to skip): ")
            password = input("Enter new password (or press Enter to skip): ")
            admin.update_admin(
                name=name if name else None,
                email=email if email else None,
                password=password if password else None
            )
        
        elif choice == "3":
            # Create New Admin
            print("\n--- Create New Admin ---")
            new_id = input("Enter new admin ID: ")
            new_pass = input("Enter password: ")
            new_name = input("Enter name: ")
            new_email = input("Enter email: ")
            Admin.create_admin(new_id, new_pass, new_name, new_email)
        
        elif choice == "4":
            # List All Admins
            Admin.list_all_admins()
        
        elif choice == "5":
            # Add Student
            print("\n--- Add Student ---")
            uid = input("Enter student UID: ")
            roll = input("Enter roll number: ")
            name = input("Enter student name: ")
            class_name = input("Enter class: ")
            marks = input("Enter marks (optional): ")
            Student.create_student(uid, roll, name, class_name, marks)
        
        elif choice == "6":
            # Remove Student
            uid = input("\nEnter student UID to remove: ")
            student = Student(uid)
            if student.student:
                confirm = input(f"Are you sure you want to delete student {student.student[2]}? (yes/no): ")
                if confirm.lower() == "yes":
                    student.delete_student()
        
        elif choice == "7":
            # View All Students
            Student.list_all_students()
        
        elif choice == "8":
            # Update Student
            print("\n--- Update Student ---")
            uid = input("Enter student UID: ")
            student = Student(uid)
            if student.student:
                roll = input("Enter new roll number (or press Enter to skip): ")
                name = input("Enter new name (or press Enter to skip): ")
                class_name = input("Enter new class (or press Enter to skip): ")
                marks = input("Enter new marks (or press Enter to skip): ")
                student.update_student(
                    roll_number=roll if roll else None,
                    name=name if name else None,
                    class_name=class_name if class_name else None,
                    marks=marks if marks else None
                )
        
        elif choice == "9":
            # Search Student by Name
            name = input("\nEnter student name to search: ")
            admin.search_student_by_name(name)
        
        elif choice == "10":
            # Add Teacher
            print("\n--- Add Teacher ---")
            emp_id = input("Enter teacher employee ID: ")
            name = input("Enter teacher name: ")
            class_name = input("Enter class: ")
            Teacher.create_teacher(emp_id, name, class_name)
        
        elif choice == "11":
            # Remove Teacher
            emp_id = input("\nEnter teacher employee ID to remove: ")
            teacher = Teacher(emp_id)
            if teacher.employee:
                confirm = input(f"Are you sure you want to delete teacher {teacher.employee[1]}? (yes/no): ")
                if confirm.lower() == "yes":
                    teacher.delete_teacher()
        
        elif choice == "12":
            # View All Teachers
            Teacher.list_all_teachers()
        
        elif choice == "13":
            # Update Teacher
            print("\n--- Update Teacher ---")
            emp_id = input("Enter teacher employee ID: ")
            teacher = Teacher(emp_id)
            if teacher.employee:
                name = input("Enter new name (or press Enter to skip): ")
                class_name = input("Enter new class (or press Enter to skip): ")
                teacher.update_teacher(
                    name=name if name else None,
                    class_name=class_name if class_name else None
                )
        
        elif choice == "14":

            name = input("\nEnter teacher name to search: ")
            admin.search_teacher_by_name(name)
        
        elif choice == "15":

            class_name = input("\nEnter class name: ")
            admin.generate_class_report(class_name)
        
        elif choice == "16":
            # View Top Students
            n = input("\nEnter number of top students to display (default 5): ")
            admin.get_top_students(int(n) if n else 5)
        
        elif choice == "17":

            admin.get_system_statistics()
        
        elif choice == "18":

            print("\n--- Export Class Data ---")
            class_name = input("Enter class name: ")
            filename = input("Enter filename (e.g., class_10A.csv): ")
            admin.export_class_data(class_name, filename)
        
        elif choice == "19":

            class_name = input("\nEnter class name to delete all students: ")
            confirm = input(f"Are you sure you want to delete ALL students from {class_name}? (yes/no): ")
            if confirm.lower() == "yes":
                admin.bulk_delete_students_by_class(class_name)
        
        elif choice == "20":
            # Logout
            print("\nLogging out...")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

def handle_student_operations():
    """Handle student operations"""
    while True:
        display_student_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            # Create New Student
            print("\n--- Create New Student ---")
            uid = input("Enter student UID: ")
            roll = input("Enter roll number: ")
            name = input("Enter student name: ")
            class_name = input("Enter class: ")
            marks = input("Enter marks (optional): ")
            Student.create_student(uid, roll, name, class_name, marks)
        
        elif choice == "2":
            # View Student Details
            uid = input("\nEnter student UID: ")
            student = Student(uid)
            if student.student:
                student.read_student()
        
        elif choice == "3":
            # Update Student Details
            print("\n--- Update Student Details ---")
            uid = input("Enter student UID: ")
            student = Student(uid)
            if student.student:
                roll = input("Enter new roll number (or press Enter to skip): ")
                name = input("Enter new name (or press Enter to skip): ")
                class_name = input("Enter new class (or press Enter to skip): ")
                marks = input("Enter new marks (or press Enter to skip): ")
                student.update_student(
                    roll_number=roll if roll else None,
                    name=name if name else None,
                    class_name=class_name if class_name else None,
                    marks=marks if marks else None
                )
        
        elif choice == "4":
            # Check Student Marks
            uid = input("\nEnter student UID: ")
            student = Student(uid)
            if student.student:
                student.check_marks()
        
        elif choice == "5":
            # Update Student Marks
            uid = input("\nEnter student UID: ")
            student = Student(uid)
            if student.student:
                marks = input("Enter new marks: ")
                student.update_marks(marks)
        
        elif choice == "6":
            # Delete Student
            uid = input("\nEnter student UID: ")
            student = Student(uid)
            if student.student:
                confirm = input(f"Are you sure you want to delete student {student.student[2]}? (yes/no): ")
                if confirm.lower() == "yes":
                    student.delete_student()
        
        elif choice == "7":
            # List All Students
            Student.list_all_students()
        
        elif choice == "8":
            # Search Student by Name
            name = input("\nEnter student name to search: ")
            Student.search_by_name(name)
        
        elif choice == "9":
            # Get Class Average
            class_name = input("\nEnter class name: ")
            Student.get_class_average(class_name)
        
        elif choice == "10":
            # Back to Main Menu
            print("\nReturning to main menu...")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

def handle_teacher_operations():
    """Handle teacher operations"""
    while True:
        display_teacher_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            # Create New Teacher
            print("\n--- Create New Teacher ---")
            emp_id = input("Enter teacher employee ID: ")
            name = input("Enter teacher name: ")
            class_name = input("Enter class: ")
            Teacher.create_teacher(emp_id, name, class_name)
        
        elif choice == "2":
            # View Teacher Details
            emp_id = input("\nEnter teacher employee ID: ")
            teacher = Teacher(emp_id)
            if teacher.employee:
                teacher.read_teacher()
        
        elif choice == "3":
            # Update Teacher Details
            print("\n--- Update Teacher Details ---")
            emp_id = input("Enter teacher employee ID: ")
            teacher = Teacher(emp_id)
            if teacher.employee:
                name = input("Enter new name (or press Enter to skip): ")
                class_name = input("Enter new class (or press Enter to skip): ")
                teacher.update_teacher(
                    name=name if name else None,
                    class_name=class_name if class_name else None
                )
        
        elif choice == "4":
            # Delete Teacher
            emp_id = input("\nEnter teacher employee ID: ")
            teacher = Teacher(emp_id)
            if teacher.employee:
                confirm = input(f"Are you sure you want to delete teacher {teacher.employee[1]}? (yes/no): ")
                if confirm.lower() == "yes":
                    teacher.delete_teacher()
        
        elif choice == "5":
            # List All Teachers
            Teacher.list_all_teachers()
        
        elif choice == "6":
            # Back to Main Menu
            print("\nReturning to main menu...")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

def initialize_system():
    """Initialize system and create default admin if needed"""
    print("\n" + "="*60)
    print(" "*10 + "Welcome to School Management System!")
    print("="*60)
    
    # Create default admin if admins.csv doesn't exist
    try:
        with open("admins.csv", "r"):
            pass
    except FileNotFoundError:
        print("\n⚠️  No admin accounts found. Creating default admin...")
        Admin.create_admin("admin", "admin123", "Default Admin", "admin@school.com")
        print("\n✅ Default admin created!")
        print("   ID: admin")
        print("   Password: admin123")
        print("\n⚠️  Please change the default password after first login.")

def main():
    """Main function"""
    initialize_system()
    
    while True:
        display_main_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            # Admin Login
            handle_admin_operations()
        
        elif choice == "2":
            # Student Operations
            handle_student_operations()
        
        elif choice == "3":
            # Teacher Operations
            handle_teacher_operations()
        
        elif choice == "4":
            # Exit
            print("\n" + "="*60)
            print(" "*10 + "Thank you for using our system!")
            print(" "*15 + "Goodbye! 👋")
            print("="*60)
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()