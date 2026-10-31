
# The Kiran Academy - Student Management System

students_data = {
    's101': {'name': 'Pranav Patil', 'city': 'Pune', 'course': 'Data Analytics'},
    's102': {'name': 'Rahul Mane', 'city': 'Mumbai', 'course': 'Data Science'},
    's103': {'name': 'Sayali Patil', 'city': 'Nagpur', 'course': 'Data Analytics'},
    's104': {'name': 'Om More', 'city': 'Nashik', 'course': 'Python Full Stack'},
    's105': {'name': 'Pooja Deshmukh', 'city': 'Pune', 'course': 'Data Analytics'},
    's106': {'name': 'Rohit Patil', 'city': 'Aurangabad', 'course': 'Data Science'},
    's107': {'name': 'Samruddhi More', 'city': 'Solapur', 'course': 'Python Full Stack'},
    's108': {'name': 'Kunal Jadhav', 'city': 'Kolhapur', 'course': 'Data Science'},
    's109': {'name': 'Anjali More', 'city': 'Satara', 'course': 'Python Full Stack'},
    's110': {'name': 'Vikas Pawar', 'city': 'Pune', 'course': 'Data Analytics'}
}

COURSES = ['Data Analytics', 'Data Science', 'Python Full Stack']

attendance = {course: {} for course in COURSES}
result = {}

users = {
    'trainer': {'om': 'om123'},
    'student': {
        's101': 'pranav123',
        's102': 'rahul123',
        's103': 'sayali123',
        's104': 'om123',
        's105': 'pooja123',
        's106': 'rohit123',
        's107' : 'samruddhi123',
        's108':'kunal123',
        's109': 'anjali123',
        's110':'vikas123'
    }
}

test = {
    'Data Analytics': {
        'Python is': {
            'options': {
                1: 'static programming language',
                2: 'dynamic programming language',
                3: 'markup language',
                4: 'database language'
            },
            'correct ans': 2
        },
        'Which library is used for data analysis in Python?': {
            'options': {
                1: 'Tkinter',
                2: 'Pandas',
                3: 'Flask',
                4: 'Pygame'
            },
            'correct ans': 2
        },
        'Which function is used to read CSV file in pandas?': {
            'options': {
                1: 'read_csv()',
                2: 'open_csv()',
                3: 'csv_read()',
                4: 'load_csv()'
            },
            'correct ans': 1
        }
    },

    'Data Science': {
        'Machine Learning is a part of': {
            'options': {
                1: 'Cyber Security',
                2: 'Networking',
                3: 'Data Science',
                4: 'UI Designing'
            },
            'correct ans': 3
        },
        'Which library is used for Machine Learning in Python?': {
            'options': {
                1: 'Flask',
                2: 'Scikit-learn',
                3: 'Tkinter',
                4: 'BeautifulSoup'
            },
            'correct ans': 2
        },
        'Which type of learning uses labeled data?': {
            'options': {
                1: 'Unsupervised Learning',
                2: 'Reinforcement Learning',
                3: 'Deep Learning',
                4: 'Supervised Learning'
            },
            'correct ans': 4
        }
    },

    'Python Full Stack': {
        'Django is a': {
            'options': {
                1: 'Database',
                2: 'Python Framework',
                3: 'Browser',
                4: 'Compiler'
            },
            'correct ans': 2
        },
        'HTML stands for': {
            'options': {
                1: 'Hyper Text Markup Language',
                2: 'High Transfer Machine Language',
                3: 'Home Tool Markup Language',
                4: 'Hyperlink Text Management Language'
            },
            'correct ans': 1
        },
        'CSS is used for': {
            'options': {
                1: 'Database Connection',
                2: 'Game Design',
                3: 'Styling Web Pages',
                4: 'Backend Logic'
            },
            'correct ans': 3
        }
    }
}


def choose_course():
    print("\nSelect Course:")
    for i, course in enumerate(COURSES, start=1):
        print(f"{i}. {course}")

    try:
        choice = int(input("Enter course choice: "))
        if 1 <= choice <= len(COURSES):
            return COURSES[choice - 1]
    except ValueError:
        pass

    print("Invalid course choice!")
    return None


def show_students():
    print("-" * 90)
    print(f"|{'RegNo':^10}|{'Name':^22}|{'City':^18}|{'Course':^32}|")
    print("-" * 90)

    for reg, details in students_data.items():
        print(
            f"|{reg:^10}|{details['name']:^22}|"
            f"{details['city']:^18}|{details['course']:^32}|"
        )

    print("-" * 90)


def take_attendance():
    course = choose_course()
    if course is None:
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not date:
        print("Date cannot be empty!")
        return

    attendance[course].setdefault(date, {})

    for reg, details in students_data.items():
        if details['course'] != course:
            continue

        print(f"\n{reg} - {details['name']}")

        while True:
            try:
                choice = int(input("1. Present  2. Absent: "))
                if choice in (1, 2):
                    break
            except ValueError:
                pass

            print("Enter 1 or 2 only.")

        attendance[course][date][reg] = (
            'Present' if choice == 1 else 'Absent'
        )

    print("\nAttendance saved successfully!")


def show_attendance():
    course = choose_course()
    if course is None:
        return

    records = attendance[course]

    if not records:
        print("No attendance records found.")
        return

    for date, details in records.items():
        print(f"\n--- Attendance: {date} ---")

        for reg, status in details.items():
            name = students_data[reg]['name']
            print(f"{reg} - {name} - {status}")


def create_test():
    course = choose_course()
    if course is None:
        return

    while True:
        question = input("\nEnter question (or 'done' to finish): ").strip()

        if question.lower() == 'done':
            break

        if not question:
            print("Question cannot be empty!")
            continue

        options = {}
        for i in range(1, 5):
            options[i] = input(f"Enter option {i}: ").strip()

        while True:
            try:
                correct_ans = int(input("Enter correct option (1-4): "))
                if correct_ans in options:
                    break
            except ValueError:
                pass

            print("Please enter a number between 1 and 4.")

        test[course][question] = {
            'options': options,
            'correct ans': correct_ans
        }

        print("Question added successfully!")


def show_results():
    if not result:
        print("No test results available.")
        return

    course = choose_course()
    if course is None:
        return

    print(f"\n--- Results: {course} ---")

    found = False
    for reg, details in result.items():
        if details['course'] == course:
            found = True
            print(
                f"{reg} | {details['name']} | "
                f"{details['marks']}/{details['total']} | "
                f"{details['percentage']:.2f}%"
            )

    if not found:
        print("No results found for this course.")


def attempt_test(reg):
    student = students_data[reg]
    course = student['course']
    questions = test[course]

    if not questions:
        print("No test available for your course.")
        return

    print(f"\n--- {course} Test ---")
    marks = 0
    total = len(questions)

    for number, (question, details) in enumerate(
        questions.items(), start=1
    ):
        print(f"\nQ{number}. {question}")

        for option_no, option_text in details['options'].items():
            print(f"{option_no}. {option_text}")

        while True:
            try:
                answer = int(input("Enter answer (1-4): "))
                if answer in (1, 2, 3, 4):
                    break
            except ValueError:
                pass

            print("Please enter 1, 2, 3, or 4.")

        if answer == details['correct ans']:
            marks += 1

    percentage = (marks / total) * 100

    result[reg] = {
        'name': student['name'],
        'course': course,
        'marks': marks,
        'total': total,
        'percentage': percentage
    }

    print("\n------ TEST RESULT ------")
    print(f"Name       : {student['name']}")
    print(f"Course     : {course}")
    print(f"Marks      : {marks}/{total}")
    print(f"Percentage : {percentage:.2f}%")


def student_attendance(reg):
    course = students_data[reg]['course']
    records = attendance[course]

    if not records:
        print("No attendance records available.")
        return

    present = sum(
        1 for daily_records in records.values()
        if daily_records.get(reg) == 'Present'
    )

    total_days = sum(
        1 for daily_records in records.values()
        if reg in daily_records
    )

    percentage = (present / total_days * 100) if total_days else 0

    print(f"\nName       : {students_data[reg]['name']}")
    print(f"Course     : {course}")
    print(f"Present    : {present}")
    print(f"Total days : {total_days}")
    print(f"Percentage : {percentage:.2f}%")


def trainer_dashboard():
    while True:
        print("\n" + " Trainer Dashboard ".center(45, "-"))
        print("""
1. Show Student Details
2. Take Attendance
3. Show Attendance
4. Create Test
5. Test Results
6. Logout
""")

        try:
            choice = int(input("Select your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            show_students()
        elif choice == 2:
            take_attendance()
        elif choice == 3:
            show_attendance()
        elif choice == 4:
            create_test()
        elif choice == 5:
            show_results()
        elif choice == 6:
            print("Trainer logged out successfully.")
            break
        else:
            print("Invalid choice!")


def student_dashboard(reg):
    while True:
        print("\n" + " Student Dashboard ".center(45, "-"))
        print("""
1. Attempt Test
2. Show Attendance
3. Show My Result
4. Logout
""")

        try:
            choice = int(input("Select your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            attempt_test(reg)
        elif choice == 2:
            student_attendance(reg)
        elif choice == 3:
            if reg in result:
                details = result[reg]
                print(f"Name: {details['name']}")
                print(f"Course: {details['course']}")
                print(f"Marks: {details['marks']}/{details['total']}")
                print(f"Percentage: {details['percentage']:.2f}%")
            else:
                print("You have not attempted the test yet.")
        elif choice == 4:
            print("Student logged out successfully.")
            break
        else:
            print("Invalid choice!")


def main():
    while True:
        print("\n" + " The Kiran Academy ".center(50, "-"))
        print("""
1. Trainer Login
2. Student Login
3. Exit
""")

        try:
            role_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if role_choice == 3:
            print("Thank you for using the system!")
            break

        if role_choice == 1:
            role = 'trainer'
        elif role_choice == 2:
            role = 'student'
        else:
            print("Invalid choice!")
            continue

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if users[role].get(username) != password:
            print("Invalid username or password!")
            continue

        if role == 'trainer':
            trainer_dashboard()
        else:
            if username not in students_data:
                print("Student record not found!")
                continue

            student_dashboard(username)


if __name__ == "__main__":
    main()