import random


# To simplify making examples, we made a helper function that randomly produces
# a list of courses and list of students/their preferences:
def randomize_example(courses, students):
    """
    Creates a random set of students, their preferred courses, and available courses for the semester.

    Args:
        - courses: A list of courses that we randomly choose from to make a list of random courses.
        - students: A list of students that we randomly choose from to make an list of random students.

    Returns:
        - A list of available courses
        - A dictionary of students and their preferred courses
    """
    num_avail_courses = random.randint(
        5, len(courses)
    )  # chooses the number of available courses this sem
    avail_courses = random.sample(
        courses, num_avail_courses
    )  # randomly chooses courses based on num of courses

    num_students = random.randint(
        5, len(students)
    )  # randomly chooses number of students this sem
    avail_students = random.sample(
        students, num_students
    )  # randomly chooses which students

    student_dict = {}

    # creates a dictionary of students with randomized num of preferred courses
    for student in avail_students:
        num_prefer = random.randint(1, 5)
        student_dict[student] = set(random.sample(avail_courses, num_prefer))

    return avail_courses, student_dict


# This is a helper function to display the schedule in an easy-to-read way
def display_schedule(schedule, time_slot_mapping):
    """Displays the schedule in a readable format, grouping courses by time slot."""
    time_slot_courses = {}

    for course, time_slot in schedule.items():
        if time_slot not in time_slot_courses:
            time_slot_courses[time_slot] = []
        time_slot_courses[time_slot].append(course)

    print("\n===== Optimized Course Schedule =====")
    for time_slot in sorted(time_slot_courses.keys()):
        print(f"{time_slot_mapping[time_slot]}: {', '.join(time_slot_courses[time_slot])}")
    print("=====================================")
