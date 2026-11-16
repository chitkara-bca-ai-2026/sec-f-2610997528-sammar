print("="*50)
print("      SCHOOL RESULT PROCESSING")
print("="*50)

# 1. Accept student details
name = input("Enter Student Name : ")
roll = input("Enter Roll Number  : ")

print("\n--- Enter Marks for 5 Subjects (0-100) ---")
marks = []
is_failed = False

# 2. Input marks for 5 subjects using a loop
for i in range(1, 6):
    m = float(input(f"Enter marks for Subject {i}: "))

    # Validate each mark
    if m < 0 or m > 100:
        print("Error: Marks should be between 0 and 100!")
        exit()

    # Check passing status: below 40 is fail
    if m < 40:
        is_failed = True

    marks.append(m)

# 3. Calculate total and percentage
total = sum(marks)
percentage = (total / 500) * 100

# 4. Assign Grade & Remark using if-elif-else
if is_failed:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remarks = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remarks = "Good"
    elif percentage >= 50:
        grade = "D"
        remarks = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remarks = "Pass"
    else:
        grade = "F"
        remarks = "Fail"

# 5. Display formatted Report Card
print("\n" + "="*50)
print("          STUDENT REPORT CARD")
print("="*50)
print(f" Student Name : {name}")
print(f" Roll Number  : {roll}")
print("-"*50)
print(f" Total Marks  : {total} / 500.0")
print(f" Percentage   : {percentage:.2f}%")
print(f" Result       : {result}")
print(f" Grade        : {grade}")
print(f" Remarks      : {remarks}")
print("="*50)