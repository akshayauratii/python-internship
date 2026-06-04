
def attendance_percentage(attended, total):
    return (attended / total) * 100

attended = int(input("Enter Classes Attended: "))
total = int(input("Enter Total Classes Conducted: "))

percentage = attendance_percentage(attended, total)

print(f"\nAttendance Percentage: {percentage:.2f}%")

if percentage >= 75:
    print("Requirement Met")
else:
    needed = 0
    while ((attended + needed) / (total + needed)) * 100 < 75:
        needed += 1

    print("Requirement Not Met")
    print("Classes needed to reach 75 attendance:", needed)
    