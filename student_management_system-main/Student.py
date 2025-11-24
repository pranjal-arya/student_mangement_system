import csv

class Student:
    def __init__(self, uid):
        self.uid = None
        self.student = None
        try:
            with open("students.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                for row in data:
                    if row[0] == uid:
                        self.uid = uid
                        self.student = row
                        print("Student fetched successfully")
                        return
            print(f"Student with UID {uid} not found")
        except FileNotFoundError:
            print("students.csv file not found")
        except Exception as e:
            print(f"Error: {e}")
    
    def read_student(self):
        if self.student:
            print(f"Student UID: {self.student[0]}\nStudent Roll Number: {self.student[1]}\nStudent Name: {self.student[2]}\nStudent Class: {self.student[3]}")
        else:
            print("Student not found!! Kindly fill the correct UID for the student")

    def update_student(self, roll_number=None, name=None, class_name=None, marks=None):
        """Update student details"""
        try:
            if not self.student:
                print("Student not found. Cannot update.")
                return False
            

            if roll_number:
                self.student[1] = roll_number
            if name:
                self.student[2] = name
            if class_name:
                self.student[3] = class_name
            if marks:
                self.student[4] = marks
            

            with open("students.csv", "r") as fileObj:
                data = list(csv.reader(fileObj))
            

            updated_data = []
            for row in data:
                if row[0] == self.uid:
                    updated_data.append(self.student)
                else:
                    updated_data.append(row)
            

            with open("students.csv", "w", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerows(updated_data)
            
            print("Student details updated successfully")
            return True
        except Exception as e:
            print(f"Error updating student: {e}")
            return False
    
    def check_marks(self):
        if self.student:
            try:
                marks = self.student[4] if len(self.student) > 4 else "No marks recorded"
                print(f"Student Name: {self.student[2]}\nStudent Roll Number: {self.student[1]}\nStudent Class: {self.student[3]}\nStudent Marks: {marks}")
            except IndexError:
                print("Marks data not available for this student")
        else:
            print("Student not found!! Kindly fill the correct UID for the student")
    
    def delete_student(self):
        """Delete student from the CSV file"""
        try:
            if not self.student:
                print("Student not found. Cannot delete.")
                return False
            
            # Read all data
            with open("students.csv", "r") as fileObj:
                data = list(csv.reader(fileObj))
            
            # Remove the specific row
            data = [row for row in data if row[0] != self.uid]
            
            # Write back to file
            with open("students.csv", "w", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerows(data)
            
            print(f"Student {self.uid} deleted successfully")
            self.student = None
            self.uid = None
            return True
        except Exception as e:
            print(f"Error deleting student: {e}")
            return False
    
    def update_marks(self, marks):
        """Update only the marks of a student"""
        try:
            if not self.student:
                print("Student not found. Cannot update marks.")
                return False
            
            # Ensure the student list has enough elements for marks
            while len(self.student) <= 4:
                self.student.append("")
            
            self.student[4] = str(marks)
            
            # Read all data
            with open("students.csv", "r") as fileObj:
                data = list(csv.reader(fileObj))
            
            # Update the specific row
            updated_data = []
            for row in data:
                if row[0] == self.uid:
                    updated_data.append(self.student)
                else:
                    updated_data.append(row)
            
            # Write back to file
            with open("students.csv", "w", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerows(updated_data)
            
            print(f"Marks updated to {marks} successfully")
            return True
        except Exception as e:
            print(f"Error updating marks: {e}")
            return False
    
    @staticmethod
    def create_student(uid, roll_number, name, class_name, marks=""):
        """Create a new student entry"""
        try:

            with open("students.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                for row in data:
                    if row[0] == uid:
                        print(f"Student with UID {uid} already exists")
                        return False
            
            with open("students.csv", "a", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerow([uid, roll_number, name, class_name, marks])
            
            print(f"Student {name} created successfully")
            return True
        except FileNotFoundError:

            with open("students.csv", "w", newline='') as fileObj:
                writer = csv.writer(fileObj)
                writer.writerow([uid, roll_number, name, class_name, marks])
            print(f"Created students.csv and added student {name}")
            return True
        except Exception as e:
            print(f"Error creating student: {e}")
            return False
    
    @staticmethod
    def list_all_students():
        """Display all students"""
        try:
            with open("students.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                print("\n--- All Students ---")
                for row in data:
                    marks = row[4] if len(row) > 4 else "N/A"
                    print(f"UID: {row[0]}, Roll: {row[1]}, Name: {row[2]}, Class: {row[3]}, Marks: {marks}")
        except FileNotFoundError:
            print("students.csv file not found")
        except Exception as e:
            print(f"Error listing students: {e}")
    
    @staticmethod
    def search_by_name(name):
        """Search students by name"""
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
        except FileNotFoundError:
            print("students.csv file not found")
        except Exception as e:
            print(f"Error searching students: {e}")
    
    @staticmethod
    def get_class_average(class_name):
        """Calculate average marks for a class"""
        try:
            with open("students.csv", "r") as fileObj:
                data = csv.reader(fileObj)
                total_marks = 0
                count = 0
                for row in data:
                    if len(row) > 3 and row[3] == class_name:
                        if len(row) > 4 and row[4]:
                            try:
                                total_marks += float(row[4])
                                count += 1
                            except ValueError:
                                continue
                
                if count > 0:
                    average = total_marks / count
                    print(f"Average marks for class {class_name}: {average:.2f}")
                    return average
                else:
                    print(f"No marks data available for class {class_name}")
                    return None
        except FileNotFoundError:
            print("students.csv file not found")
        except Exception as e:
            print(f"Error calculating average: {e}")
            return None


