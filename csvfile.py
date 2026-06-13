import csv

# Define the header and data for 10 students
header = ['Roll No', 'Name', 'Maths', 'Physics', 'Chemistry', 'English']
data = [
    [101, 'Ananya', 85, 90, 88, 92],
    [102, 'Rahul', 78, 82, 80, 85],
    [103, 'Sneha', 95, 94, 96, 92],
    [104, 'Vikram', 65, 70, 68, 72],
    [105, 'Arjun', 88, 85, 90, 87],
    [106, 'Priya', 92, 89, 91, 94],
    [107, 'Rohan', 72, 75, 70, 78],
    [108, 'Kavya', 81, 83, 85, 80],
    [109, 'Sai', 89, 91, 87, 88],
    [110, 'Divya', 76, 74, 78, 82]
]

# Writing to the CSV file
with open('student.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print("student.csv file created successfully!")


import csv

print("--- Displaying All Student Records ---")
highest_marks = -1
highest_student = ""
total_marks_all_students = 0
total_subjects_count = 0

with open('student.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    print(f"{header[0]:<10} {header[1]:<12} {header[2]:<8} {header[3]:<8} {header[4]:<10} {header[5]:<8} | Total")
    print("-" * 65)
    
    student_count = 0
    for row in reader:
        student_count += 1
        roll_no = row[0]
        name = row[1]
        
        # Convert marks from strings to integers
        marks = [int(m) for m in row[2:]]
        total_score = sum(marks)
        
        # Display the row nicely formatted
        print(f"{roll_no:<10} {name:<12} {marks[0]:<8} {marks[1]:<8} {marks[2]:<10} {marks[3]:<8} | {total_score}")
        
        # Track the highest scorer
        if total_score > highest_marks:
            highest_marks = total_score
            highest_student = name
            
        # Accumulate marks for the class average
        total_marks_all_students += total_score
        total_subjects_count += len(marks)

print("-" * 65)

# Calculations for the output
class_average = total_marks_all_students / total_subjects_count
overall_student_average = total_marks_all_students / student_count

print(f"\n> Highest Scorer: {highest_student} with a total of {highest_marks} marks.")
print(f"> Class Average Marks (per subject baseline): {class_average:.2f}")
print(f"> Average Total Marks per student: {overall_student_average:.2f}")