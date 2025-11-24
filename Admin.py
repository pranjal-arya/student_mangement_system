import csv

class Admin:
    def __init__(self, admin_id, password):
        self.admin_id = None
        self.admin_data = None
        self.is_authenticated = False
        
        try:
            with open("admins.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                for row in data:
                    if row[0] == admin_id and row[1] == password:
                        self.admin_id = admin_id
                        self.admin_data = row
                        self.is_authenticated = True
                        print(f"Admin {row[2]} logged in successfully")
                        return
                print("Invalid admin credentials")
        except FileNotFoundError:
            print("admins.csv file not found")
        except Exception as e:
            print(f"Error: {e}")
    
    def read_admin(self):
        """Display admin details"""
        if self.admin_data:
            print(f"Admin ID: {self.admin_data[0]}\nAdmin Name: {self.admin_data[2]}\nAdmin Email: {self.admin_data[3]}")
        else:
            print("Admin not authenticated")
    
    def update_admin(self, name=None, email=None, password=None):
        """Update admin details"""
        try:
            if not self.is_authenticated:
                print("Admin not authenticated. Cannot update.")
                return False
            
            # Update the admin object with new values
            if name:
                self.admin_data[2] = name
            if email:
                self.admin_data[3] = email
            if password:
                self.admin_data[1] = password
            
            # Read all data first
            with open("admins.csv", "r") as fileObj:
                data = list(csv.reader(fileObj))
            
            # Update the specific row
            updated_data = []
            for row in data:
                if row[0] == self.admin_id:
                    updated_data.append(self.admin_data)
                else:
                    updated_data.append(row)
            
            # Write back to file
            with open("admins.csv", "w", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerows(updated_data)
            
            print("Admin details updated successfully")
            return True
        except Exception as e:
            print(f"Error updating admin: {e}")
            return False
    
    def delete_admin(self):
        """Delete admin account"""
        try:
            if not self.is_authenticated:
                print("Admin not authenticated. Cannot delete.")
                return False
            
            # Read all data
            with open("admins.csv", "r") as fileObj:
                data = list(csv.reader(fileObj))
            
            # Remove the specific row
            data = [row for row in data if row[0] != self.admin_id]
            
            # Write back to file
            with open("admins.csv", "w", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerows(data)
            
            print(f"Admin {self.admin_id} deleted successfully")
            self.admin_data = None
            self.admin_id = None
            self.is_authenticated = False
            return True
        except Exception as e:
            print(f"Error deleting admin: {e}")
            return False
    
    @staticmethod
    def create_admin(admin_id, password, name, email):
        """Create a new admin account"""
        try:
            # Check if admin_id already exists
            try:
                with open("admins.csv", "r") as fileObj:
                    data = csv.reader(fileObj)
                    for row in data:
                        if row[0] == admin_id:
                            print(f"Admin with ID {admin_id} already exists")
                            return False
            except FileNotFoundError:
                pass
            
            # Append new admin
            with open("admins.csv", "a", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerow([admin_id, password, name, email])
            
            print(f"Admin {name} created successfully")
            return True
        except Exception as e:
            print(f"Error creating admin: {e}")
            return False
    
    @staticmethod
    def list_all_admins():
        """Display all admins"""
        try:
            with open("admins.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                print("\n--- All Admins ---")
                for row in data:
                    print(f"ID: {row[0]}, Name: {row[2]}, Email: {row[3]}")
        except FileNotFoundError:
            print("admins.csv file not found")
        except Exception as e:
            print(f"Error listing admins: {e}")
    
    # ==================== REPORTING AND ANALYTICS ====================
    
    def generate_class_report(self, class_name):
        """Generate a report for a specific class"""
        if not self.is_authenticated:
            print("Admin not authenticated")
            return False
        
        try:
            with open("students.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                students_in_class = []
                total_marks = 0
                count = 0
                
                for row in data:
                    if len(row) > 3 and row[3] == class_name:
                        students_in_class.append(row)
                        if len(row) > 4 and row[4]:
                            try:
                                total_marks += float(row[4])
                                count += 1
                            except ValueError:
                                pass
                
                if not students_in_class:
                    print(f"No students found in class {class_name}")
                    return False
                
                print(f"\n--- Class Report: {class_name} ---")
                print(f"Total Students: {len(students_in_class)}")
                
                if count > 0:
                    average = total_marks / count
                    print(f"Average Marks: {average:.2f}")
                else:
                    print("No marks data available")
                
                print("\nStudent List:")
                for student in students_in_class:
                    marks = student[4] if len(student) > 4 else "N/A"
                    print(f"  UID: {student[0]}, Roll: {student[1]}, Name: {student[2]}, Marks: {marks}")
                
                return True
        except Exception as e:
            print(f"Error generating class report: {e}")
            return False
    
    def get_top_students(self, n=5):
        """Get top N students by marks"""
        if not self.is_authenticated:
            print("Admin not authenticated")
            return False
        
        try:
            with open("students.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                students_with_marks = []
                
                for row in data:
                    if len(row) > 4 and row[4]:
                        try:
                            marks = float(row[4])
                            students_with_marks.append((row, marks))
                        except ValueError:
                            pass
                
                if not students_with_marks:
                    print("No students with marks data found")
                    return False
                
                # Sort by marks in descending order
                students_with_marks.sort(key=lambda x: x[1], reverse=True)
                
                print(f"\n--- Top {n} Students ---")
                for i, (student, marks) in enumerate(students_with_marks[:n], 1):
                    print(f"{i}. {student[2]} (Class {student[3]}) - {marks} marks")
                
                return True
        except Exception as e:
            print(f"Error getting top students: {e}")
            return False
    
    def get_system_statistics(self):
        """Get overall system statistics"""
        if not self.is_authenticated:
            print("Admin not authenticated")
            return False
        
        try:
            # Count students
            student_count = 0
            try:
                with open("students.csv", "r") as fileObj:
                    student_count = sum(1 for _ in csv.reader(fileObj))
            except FileNotFoundError:
                pass
            
            # Count teachers
            teacher_count = 0
            try:
                with open("teachers.csv", "r") as fileObj:
                    teacher_count = sum(1 for _ in csv.reader(fileObj))
            except FileNotFoundError:
                pass
            
            # Count admins
            admin_count = 0
            try:
                with open("admins.csv", "r") as fileObj:
                    admin_count = sum(1 for _ in csv.reader(fileObj))
            except FileNotFoundError:
                pass
            
            print("\n--- System Statistics ---")
            print(f"Total Students: {student_count}")
            print(f"Total Teachers: {teacher_count}")
            print(f"Total Admins: {admin_count}")
            
            return True
        except Exception as e:
            print(f"Error getting system statistics: {e}")
            return False
    
    def search_student_by_name(self, name):
        """Search for students by name"""
        if not self.is_authenticated:
            print("Admin not authenticated")
            return False
        
        try:
            with open("students.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                found = False
                print(f"\n--- Students matching '{name}' ---")
                for row in data:
                    if name.lower() in row[2].lower():
                        marks = row[4] if len(row) > 4 else "N/A"
                        print(f"UID: {row[0]}, Roll: {row[1]}, Name: {row[2]}, Class: {row[3]}, Marks: {marks}")
                        found = True
                if not found:
                    print("No students found with that name")
                return found
        except Exception as e:
            print(f"Error searching students: {e}")
            return False
    
    def search_teacher_by_name(self, name):
        """Search for teachers by name"""
        if not self.is_authenticated:
            print("Admin not authenticated")
            return False
        
        try:
            with open("teachers.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                found = False
                print(f"\n--- Teachers matching '{name}' ---")
                for row in data:
                    if name.lower() in row[1].lower():
                        print(f"ID: {row[0]}, Name: {row[1]}, Class: {row[2]}")
                        found = True
                if not found:
                    print("No teachers found with that name")
                return found
        except Exception as e:
            print(f"Error searching teachers: {e}")
            return False
    
    def export_class_data(self, class_name, filename):
        """Export class data to a separate CSV file"""
        if not self.is_authenticated:
            print("Admin not authenticated")
            return False
        
        try:
            with open("students.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                students_in_class = [row for row in data if len(row) > 3 and row[3] == class_name]
            
            if not students_in_class:
                print(f"No students found in class {class_name}")
                return False
            
            with open(filename, "w", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerows(students_in_class)
            
            print(f"Class {class_name} data exported to {filename}")
            return True
        except Exception as e:
            print(f"Error exporting data: {e}")
            return False
    
    def bulk_delete_students_by_class(self, class_name):
        """Delete all students from a specific class"""
        if not self.is_authenticated:
            print("Admin not authenticated")
            return False
        
        try:
            # Read all data
            with open("students.csv", "r") as fileObj:
                data = list(csv.reader(fileObj))
            
            original_count = len(data)
            # Remove students from the specific class
            data = [row for row in data if len(row) <= 3 or row[3] != class_name]
            
            deleted_count = original_count - len(data)
            
            if deleted_count == 0:
                print(f"No students found in class {class_name}")
                return False
            
            # Write back to file
            with open("students.csv", "w", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerows(data)
            
            print(f"{deleted_count} student(s) from class {class_name} deleted successfully")
            return True
        except Exception as e:
            print(f"Error deleting students: {e}")
            return False