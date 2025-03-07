from algorithm import tabu_search
from helpers import randomize_example
import matplotlib.pyplot as plt


def sweep_single_input(course_list, student_list, time_slots, num_runs):
    """
    Runs our algorithm `num_runs` times on a randomized input and returns a list of scores.

    Args:
    - course_list: A list of courses that we use to create randomized input.
    - student_list: A list of students that we use to create randomized input.
    - time_slots: A list of integers representing the time slots.
    - num_runs: Int representing number of times search will run.

    Returns:
        - The list of scores generated running the algorithm.
    """
    score_list = []
    c, s = randomize_example(course_list, student_list)

    for i in range(num_runs):
        optim_sched, best_score = tabu_search(c, s, time_slots)
        score_list.append(best_score)
    return score_list


def sweep_randomized_inputs(course_list, student_list, time_slots, num_runs):
    """
    Runs our algorithm `num_runs` times, generating a new randomized input on each run, and returns a list of scores.

    Args:
    - course_list: A list of courses that we use to create randomized input.
    - student_list: A list of students that we use to create randomized input.
    - time_slots: A list of integers representing the time slots.
    - num_runs: Int representing number of times search will run.

    Returns:
        - The list of scores generated running the algorithm.
    """
    score_list = []

    for i in range(num_runs):
        c, s = randomize_example(course_list, student_list)
        optim_sched, best_score = tabu_search(c, s, time_slots)
        score_list.append(best_score)
    return score_list



def plot_scores(score_list, num_runs):
    """
    Plot the results of running the search on randomized inputs for a number of runs.

    Args:
    - score_list: A list of scores.
    - num_runs: Int representing number of times search will run.
    """

    plt.plot(score_list)
    plt.ylim(0, 100)

    # Add labels and title
    plt.xlabel("Runs")
    plt.ylabel("Scores (%)")
    plt.title(f"Scores Over {num_runs} Runs")

    # Show the plot
    plt.show()
