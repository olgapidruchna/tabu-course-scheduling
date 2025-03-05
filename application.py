from algorithm import tabu_search

courses = [
    "ENGR3415",
    "ENGR3333",
    "MTH2133",
    "AHS1256",
    "AHS8535",
    "BIO301",
    "ENGR1690",
    "SCOPE",
    "FRST101",
]
time_slots = [1, 2, 3, 4, 5]

# """
# 1 - MR 1 pm
# 2 - MR 2:50 pm
# 3 - TF 1 pm
# 4 - TF 2:50 pm
# 5 - W
# """

student_courses = {
    "Lily": {"ENGR3415", "MTH2133", "BIO301"},
    "Madie": {"ENGR3415", "ENGR3333", "AHS8535"},
    "Olga": {"ENGR3333", "MTH2133", "ENGR1690"},
    "Amit": {"AHS1256", "MTH2133", "BIO301"},
    "Anmol": {"ENGR1690", "AHS1256", "ENGR3415"},
    "Franklin": {"FRST101"},
}

best_schedule, best_score = tabu_search(courses, student_courses, time_slots)

print("Optimized Schedule:", best_schedule)
print("Total Conflict-Free Course Assignments:", best_score)
