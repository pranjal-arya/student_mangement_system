import csv

class Teacher:
    def __init__(self, employee_id):
        try:
            with open("teachers.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                for rows in data:
                    if rows[0] == employee_id:
                        self.employee_id = employee_id
                        self.employee = rows
                        return

                self.employee_id = None
                self.employee = None
        except Exception as e:
            print(f"Error reading file: {e}")
            self.employee_id = None
            self.employee = None
    
    def read_teacher(self):
        try:
            if self.employee:
                print(f"Teacher's Employee ID: {self.employee_id}\nTeacher's Name: {self.employee[1]}\nTeacher's Class: {self.employee[2]}")
            else:
                print("Teacher not found")
        except Exception as e:
            print(f"Error: {e}")
    
    def update_teacher(self, name=None, class_name=None):
        """Update teacher's name and/or class"""
        try:
            if not self.employee:
                print("Teacher not found. Cannot update.")
                return False
            

            if name:
                self.employee[1] = name
            if class_name:
                self.employee[2] = class_name
            

            with open("teachers.csv", "r") as fileObj:
                data = list(csv.reader(fileObj))
            

            for i, row in enumerate(data):
                if row[0] == self.employee_id:
                    data[i] = self.employee
                    break
            

            with open("teachers.csv", "w", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerows(data)
            
            print("Teacher updated successfully")
            return True
        except Exception as e:
            print(f"Error updating teacher: {e}")
            return False
    
    def delete_teacher(self):
        """Delete teacher from the CSV file"""
        try:
            if not self.employee:
                print("Teacher not found. Cannot delete.")
                return False
            

            with open("teachers.csv", "r") as fileObj:
                data = list(csv.reader(fileObj))
            

            data = [row for row in data if row[0] != self.employee_id]
            

            with open("teachers.csv", "w", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerows(data)
            
            print(f"Teacher {self.employee_id} deleted successfully")
            self.employee = None
            self.employee_id = None
            return True
        except Exception as e:
            print(f"Error deleting teacher: {e}")
            return False
    
    @staticmethod
    def create_teacher(employee_id, name, class_name):
        """Create a new teacher entry"""
        try:

            with open("teachers.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                for row in data:
                    if row[0] == employee_id:
                        print(f"Teacher with ID {employee_id} already exists")
                        return False
            

            with open("teachers.csv", "a", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerow([employee_id, name, class_name])
            
            print(f"Teacher {name} created successfully")
            return True
        except Exception as e:
            print(f"Error creating teacher: {e}")
            return False
    
    @staticmethod
    def list_all_teachers():
        """Display all teachers"""
        try:
            with open("teachers.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                print("\n--- All Teachers ---")
                for row in data:
                    print(f"ID: {row[0]}, Name: {row[1]}, Class: {row[2]}")
        except Exception as e:
            print(f"Error listing teachers: {e}")


