print("===== STUDENT GRADE MANAGEMENT SYSTEM =====")

print("1. Add Student.")
print("2. Display Students.")
print("3. Search Student.")
print("4. Find Topper.")
print("5. Exit")

students=[]

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def calculate_average(self):
        if not self.marks:
            return 0
        total=sum(self.marks)
        avg=total/len(self.marks)
        return avg

    def display_details(self):
        print("Name : ",self.name)
        print("Roll No : ",self.roll_no)
        print("Marks : ",self.marks)
        print("Average : ",self.calculate_average())

    def has_roll_no(self,roll_no):
        if self.roll_no==roll_no:
            return self.roll_no==roll_no

while True:
    while True:
        try:
            choice=int(input("Select the choice: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice==5:
        break
    elif choice<=0 or choice>5:
        print("Invalid choice.Select again..")
        continue
    else:
        match choice:
            case 1:
                name=input("Student Name: ")
                roll_no=int(input("Roll No: "))
                marks=(input("Marks: "))
                marks_list=[int(x) for x in marks.split()]
                new_student=Student(name,roll_no,marks_list)
                found =False
                for student in students:
                    if student.has_roll_no(roll_no):
                        found=True
                        print("Roll number already exists!")
                        print("Student is not added.")
                        break
                if not found:
                    students.append(new_student)
                    print("Student added Successfully....")
                        
            case 2:
                if not students:
                    print("No students found..")
                else:
                    for student in students:
                        student.display_details()
            case 3:
                roll_no=int(input("Enter the Roll No : "))
                found=False
                for student in students:
                    if student.has_roll_no(roll_no):
                        found=True
                        print("Student Found!")
                        student.display_details()
                        break
                if not found:
                    print("Student not found.")
            case 4:
                if not students:
                    print("No students found.")
                else:
                    topper=None
                    max_avg=0
                    for student in students:
                        avg=student.calculate_average()
                        if avg>max_avg:
                            max_avg=avg
                            topper=student.name
                    print("Topper : ",topper)
                    print("Average : ",max_avg)
