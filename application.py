from algorithm import tabu_search
import random


# The following are the inputs to the tabu search algorithm:

# 1) The courses available this semester. This would look like the following:
example_courses = [
    "ENGR3415",
    "ENGR3333",
    "MTH2133",
    "AHS1256",
    "AHS8535",
    "BIO301",
    "ENGR1690",
    "SCOPE",
]

# 2) A dictionary of students and their preferred courses.
# This is an example of what this would look like:
example_student_pref = {
    "Lily": {"ENGR3415", "MTH2133", "BIO301"},
    "Madie": {"ENGR3415", "ENGR3333", "AHS8535"},
    "Olga": {"ENGR3333", "MTH2133", "ENGR1690"},
    "Amit": {"AHS1256", "MTH2133", "BIO301"},
    "Anmol": {"ENGR1690", "AHS1256", "ENGR3415"},
    "Franklin": {"FRST101"},
}

example_students = [
    "Lily",
    "Madie",
    "Olga",
    "Amit",
]

# 3) A list of time slots, where 5 is hardcoded to be Wednesday in the algorithm.
# Each index corresponds to a time slot:
# 1 - MR 8:30 am
# 2 - MR 10 am
# 3 - TF 8:30 am
# 4 - TF 10 am
# 5 - W 10 am (SCOPE will 'run' on this time slot)
# 6 MR 1 pm
# 7 TF 1 pm
# 8 MR 2:50 pm
# 9 TF 2:50 pm
time_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Here is an example of our algorithm running:

best_schedule, best_score = tabu_search(
    example_courses, example_student_pref, time_slots
)

print("Optimized Schedule:", best_schedule)
print("Total Conflict-Free Course Assignments:", best_score)


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


course_list = [
    "ENGR3415",
    "ENGR3333",
    "MTH2133",
    "AHS1256",
    "AHS8535",
    "BIO301",
    "ENGR1690",
    "SCOPE",
    "FRST101",
    "MTH5452",
    "SCI1504",
    "BIO2039",
    "SCI5069",
    "MTH2103",
    "ENGR1204",
]

student_list = [
    "Lily",
    "Madie",
    "Olga",
    "Amit",
    "Anmol",
    "Aditi",
    "Maya",
    "Rucha",
    "Norden",
    "Milas",
    "Franklin",
]

# Here, we are running 5 examples on our algorithm and comparing their performance
score_list = []

for i in range(5):
    c, s = randomize_example(course_list, student_list)
    optim_sched, best_score = tabu_search(c, s, time_slots)
    print(f"Optimized schedule: {optim_sched}")
    print(f"Score: {best_score}")

    score_list.append(best_score)


# student_courses2 = {
#     "Lily": {"ENGR3415", "MTH2133", "BIO301", "SCOPE"},
#     "Madie": {"ENGR3415", "ENGR3333", "AHS8535", "SCI1504", "SCOPE"},
#     "Olga": {"ENGR3333", "MTH2133", "ENGR1690", "SCOPE"},
#     "Amit": {"AHS1256", "MTH2103", "BIO301"},
#     "Anmol": {"ENGR1690", "AHS1256", "ENGR3415", "SCI1504"},
#     "Franklin": {"FRST101", "MTH5452", "ENGR1204"},
#     "Milas": {"FRST101", "MTH5452", "AHS8535"},
#     "Norden": {"ENGR1204", "MTH2103", "SCI5069", "BIO2039"},
# }

# best_schedule2, best_score2 = tabu_search(courses2, student_courses2, time_slots2)

# print("Optimized Schedule:", best_schedule2)
# print("Total Conflict-Free Course Assignments:", best_score2)
