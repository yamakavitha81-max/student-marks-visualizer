import matplotlib.pyplot as plt

students = []
marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))
    
    students.append(name)
    marks.append(mark)

def bar_chart():
    plt.bar(students, marks)
    plt.title("Students Marks - Bar Chart")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.show()

def line_chart():
    plt.plot(students, marks, marker="o")
    plt.title("Students Marks - Line Chart")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.show()

def pie_chart():
    plt.pie(marks, labels=students, autopct="%1.1f%%")
    plt.title("Students Marks - Pie Chart")
    plt.show()

while True:
    print("\n===== Student Marks Dashboard =====")
    print("1. Bar Chart")
    print("2. Line Chart")
    print("3. Pie Chart")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bar_chart()

    elif choice == "2":
        line_chart()

    elif choice == "3":
        pie_chart()

    elif choice == "4":
        print("Program ended")
        break

    else:
        print("Invalid choice")
