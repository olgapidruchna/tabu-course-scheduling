import random


def conflict_free_courses(schedule, student_courses):
    """
    Serves as our evaluation function for the tabu algorithm. Finds the percentage of courses
    that do not have time conflicts based on students' listed preferred courses.

    Args:
        - schedule: A dictionary with course codes listed as keys, and the time slot as
        the value.
        - student_courses: A dictionary with students as keys and their preferred courses
        as the value.

    Returns:
        - A float representing the percentage of conflict-free
        courses there are across each student.
    """
    total_courses = 0
    total_conflict_free_courses = 0

    for _, pref_courses in student_courses.items():
        times = [schedule[course] for course in pref_courses if course in schedule]
        total_courses += len(times)
        unique_times = set(times)

        # count only non-conflicting courses
        no_conflicts = len(unique_times)
        total_conflict_free_courses += no_conflicts

    return (total_conflict_free_courses/total_courses)*100


def is_valid_solution(schedule):
    """
    This function ensures that the schedule produced follows all constraints:

        - no time slot has more than 3 courses
        - SCOPE is only scheduled on Wednesdays
        - First year courses are not scheduled on Wednesdays

    Args:
        - schedule: A dictionary representing the course codes and their time slots.

    Returns:
        - A boolean: True if the schedule is valid, False otherwise
    """
    time_slot_count = {}

    # Going through all courses in the schedule
    for course, time_slot in schedule.items():
        # check first year classes not on wed
        if "FRST" in course and time_slot == 5:
            return False

        # Increment time slot count
        if time_slot in time_slot_count:
            time_slot_count[time_slot] += 1
        else:
            time_slot_count[time_slot] = 1

    # check no more than 3 classes per slot
    if not all(count <= 3 for count in time_slot_count.values()):
        return False

    # check that SCOPE is set on Wednesday's timeslot (5)
    if "SCOPE" in schedule.keys():
        if schedule["SCOPE"] != 5:
            return False

    return True


def generate_solutions(schedule, time_slots):
    """
    Generates neighboring solutions by moving or swapping course time slots.

    Args:
        - schedule: A dictionary representing course codes and their respective
        time slots.
        - time_slots: A list of integers representing the time slot (ex: TF 1pm)

    Returns:
        - neighbors: A list of valid schedule solutions.
    """
    neighbors = []
    courses = list(schedule.keys())

    # generate multiple candidate solutions
    for _ in range(len(courses)):
        new_schedule = schedule.copy()

        # randomly moves a course to a different time slot
        if random.random() < 0.5:
            course = random.choice(courses)
            new_schedule[course] = random.choice(time_slots)

        # randomly swaps two courses' time slots
        else:
            c1, c2 = random.sample(courses, 2)
            new_schedule[c1], new_schedule[c2] = new_schedule[c2], new_schedule[c1]

        # only add valid schedules
        if is_valid_solution(new_schedule):
            neighbors.append(new_schedule)

    return neighbors


def tabu_search(courses, student_courses, time_slots, max_iter=100, tabu_size=10):
    """
    Optimizes the course schedule using Tabu Search heuristic.

    Args:
        - courses: A list of courses to optimize.
        - student_courses: A dictionary of students and their preferred courses.
        - time_slots: A list of time slots for courses to be set.
        - max_iter: An integer representing the max times to run through algorithm.
        Set to 100 by default, unless specified otherwise.
        - tabu_size: An integer representing how long the tabu list is/how many
        iterations before a solution is 'un-tabued'. Set to 10 by default.

    Returns:
        - best_solution: A dictionary representing each course and their time slot
        - best_score: An integer representing the number of conflict-free courses
        based on the students' preferred courses.
    """
    # initializes a random valid schedule to start off with
    while True:
        curr_schedule = {course: random.choice(time_slots) for course in courses}
        if is_valid_solution(curr_schedule):
            break
    # print(f"Current schedule: {curr_schedule}")

    # initializes best schedule/best score to beat
    best_schedule = curr_schedule
    best_score = conflict_free_courses(curr_schedule, student_courses)
    tabu_list = []

    for _ in range(max_iter):
        neighbors = generate_solutions(curr_schedule, time_slots)
        # print(f"Neighbors: {neighbors}")

        # evaluates neighbors and selects the best one not in tabu list
        best_neighbor = None
        best_neighbor_score = -1

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                score = conflict_free_courses(neighbor, student_courses)
                if score > best_neighbor_score:
                    best_neighbor = neighbor
                    best_neighbor_score = score

        # checks if curr sol is best global solution
        if best_neighbor:
            curr_schedule = best_neighbor
            tabu_list.append(best_neighbor)
            if len(tabu_list) > tabu_size:  # updates tabu list
                tabu_list.pop(0)

            if best_neighbor_score > best_score:
                best_schedule = best_neighbor
                best_score = best_neighbor_score

    return best_schedule, best_score
