# Optimizing College Course Scheduling with Tabu Search Algorithm

### By Olga Pidruchna and Madison Tong

## **Overview**

<!-- ### **What is it?** -->

The tabu search (TS) algorithm is a metaheuristic optimization algorithm created by Fred Glover in 1986. It belongs to the field of local search algorithms, but stands out due to its ability to escape local optima. This is achieved by maintaining a memory structure, called a "tabu list," of recently visited solutions that the algorithm is prohibited from revisiting for a specified number of iterations. The term "tabu," originates from the Tongan word meaning things that cannot be touched because they are sacred.<sup>1</sup> The TS algorithm was designed at a time when for an algorithm to be considered "intelligent," it had to incorporate either "adaptive memory" or "responsive exploration."<sup>2</sup>

One strength of tabu search is its ability to escape local optima by "tabu-ing" certain solutions. By restricting movement to previously visited solutions, TS encourages exploration of less optimal areas, preventing cycles and enabling a broader search of the solution space. This makes it effective not only in local search but also for global optimization, as it is built in a way to allow further exploration of both promising areas and new areas in the solution space. Additionally, TS is highly adaptable and can be tailored to a variety of optimization problems.

However, this algorithm has some drawbacks. Its performance is sensitive to parameter tuning, particularly the size of the tabu list. It may also require a high number of iterations to converge to a high-quality solution, making it computationally intensive. Furthermore, TS may struggle with highly constrained problems or those with a large number of local optima.

Despite these limitations, tabu search remains a powerful and versatile algorithm, compatible with the vast majority of optimization problems (problems involving maximizing or minimizing).

Some examples of common problems used with TS are: <sup>3</sup>

- Supply chain management
- Vehicle routing
- Data mining
- Traveling Salesman Problem
- DNA sequencing
- Minimum Spanning Tree (MST)

### **Design Decisions**

Implementing a tabu search algorithm involves several key design decisions that must be tailored to the specific problem.

#### Tabu Tenure

Tabu tenure determines the number of iterations a move or solution remains in the tabu list. It should be set based on the size and complexity of the problem.

- A shorter tabu tenure allows for greater exploration but increases the risk of cycling, as previously visited solutions become available again sooner.
- A longer tabu tenure promotes diversification by discouraging returns to previous solutions, but may slow the search process.

#### Aspiration Criteria

Aspiration criteria are a set of rules that determine whether a tabu move can be allowed. These criteria help prevent excessively restrictive searches and allow promising solutions to be considered even if they are tabu. Common aspiration criteria include:

- Allowing a tabu move if it leads to a solution better than the best solution found so far.
- Allowing a tabu move if it has not been visited for a certain number of iterations.

#### Stopping Criteria

Stopping criteria determine when the search terminates, returning the best solution found up to that point. There are multiple criteria that can be used that yield different results:

- **Maximum number of iterations** - Search stops after a predefined number of steps
- **Solution quality threshold** - Search stops when a solution meets a specified quality level
- **Time limit** - Search stops after fixed duration
- **No improvement** - Search stops if no better solution is found after a given number of consecutive iterations

If minimizing runtime is a priority, setting a time limit is a practical choice. If solution quality is the primary concern, a quality threshold may be used. Multiple stopping criteria can also be combined to tailor fit a problem. A common practice is to set a maximum number of iterations and terminate if no improvement occurs for a certain period.

#### Neighborhood Structure

The neighborhood structure defines how neighboring solutions are generated and explored. The neighborhood should be large enough to ensure diverse exploration but not so large that evaluating all neighbors becomes computationally expensive. The structure should be carefully designed to reflect the nature of the problem, ensuring that moves within the neighborhood contribute meaningfully to the search process.

### **How it works**

The basic process of tabu search is as follows:

1. Generate an initial/current solution `x` and set `current_best = x`. This initial solution does not need to be optimal.
2. Initialize an empty tabu list, and set the table tenure, aspiration criteria, and stopping criteria.
3. While the stopping criteria hasn't been met, rerun steps a to e:  
   _a_. Generate a set of neighboring solutions `N(x)`.  
   _b_. Select the best solution `x'` from `N(x)` that is is not in the tabu list. If all solutions are tabu, select the best one that meets the aspiration criteria.  
   _c_. Update current solution `x = x'`.  
   _d_. If `x` is better than `current_best`, update `current_best = x`.  
   _e_. Add the new `x` value to the tabu list. If tabu list exceeds the tabu tenure, remove the earliest solution from the list.
4. Return `current_best`.

Here is an additional diagram to visualize this process: <sup>4</sup>
![image](Flowchart-of-tabu-search-algorithm.png)

## **Application: Course Scheduling**

The application we chose is **college course scheduling**. The goal of our algorithm is to assign courses running in a semester to time slots in a way that maximizes student enrollment in preferred courses without scheduling conflicts. Tabu search is well-suited for this problem, as it helps find an optimal course schedule without getting trapped in local maxima.

The algorithm takes the following inputs:

- A list courses that will be offered
- Available time slots for scheduling
- A mapping of students to a list of their preferred classes

We also have constraints for a valid schedule:

- SCOPE must be scheduled on Wednesday
- First year classes cannot be scheduled on Wednesday
- No more than three courses can be scheduled in a single time slot

More constraints may be added to this list to further refine the schedule.

The quality of a schedule is evaluated by calculating the percentage of preferred courses that do not have time conflicts across all students.

### **Assumptions**

Our application of this algorithm abstracts some details regarding the problem. We assume that the courses all have classrooms to run in and faculty to teach who don't also have a conflicting schedule. The algorithm also assumes that the number of courses is less than or equal to 3 times the number of time slots. This is because we have a constraint that doesn't allow more than 3 classes per time slot, and we have no checks to ensure that we do not have to schedule more classes than there are possible slots.

In regards to assumptions with the tabu search algorithm itself, the algorithm runs on the assumption that there are local optima that must be avoided within the solution space. This is why it includes a tabu list. However if the solution space only includes a global optima, then the tabu list wouldn't be needed since there are no local optima to avoid.

### **Other Use Cases**

This algorithm can be modified to be used in many different scheduling problems. For example, it can be used for job scheduling or task scheduling. It could also be used for spatial allocation, such as organizing stock in a warehouse, or resource allocation, such as in the healthcare system.

## **Ethical Analysis**

As with all heuristic algorithms, the way that you set up parameters highly impacts the outcomes you get. If the input data contains bias, this can unintentionally created biased results. Additionally if an objective function is created to weigh a certain factor more than others, this may also have intentional biased effects. In applications such as resource allocation in hospitals, for example, biased results can even be detrimental to certain groups of patients who may be deprived of aid. In the cases of more socially nuanced problems, such as creating social policies or anything that may have impactful decisions such as disaster relief responses, the tabu search algorithm may not be taking every factor into consideration.

These concerns can be mitigated by manually checking your data beforehand and considering what biases may arise from the information presented. Additionally, having humans consider how to craft the objective function and ponder who may be affected by weighing one factor more than another will help to decrease risks of harmful effects.

One such case is the AI company FPI, based in Vietnam, who has taken part in founding the Ethical AI committee in Vietnam in order to ensure their technology's safe use and to protect their country's "commitment to ethical governance and responsible advancement of artificial intelligence." <sup>5</sup>

## Resources

1. Wikipedia Contributors. “Tabu Search.” Wikipedia, Wikimedia Foundation, 18 June 2019, en.wikipedia.org/wiki/Tabu_search.
2. Glover, Fred, and Manuel Laguna. Tabu Search. Boston, MA, Springer US, 1997.
3. Algorithmafternoon.com, 2024, algorithmafternoon.com/stochastic/tabu_search/.
4. Hao, Peng, et al. Intra-Platoon Vehicle Sequence Optimization for Eco-Cooperative Adaptive Cruise Control. 1 Oct. 2017, https://doi.org/10.1109/itsc.2017.8317879. Accessed 14 Aug. 2023.
5. “FPT to Support Vietnam’s Push for Ethical and Responsible AI Innovation.” Fptsoftware.com, 2024, fptsoftware.com/newsroom/news-and-press-releases/press-release/fpt-to-support-vietnamm-push-for-ethical-and-responsible-ai-innovation.

#### Libraries Used:

- random
- matplotlib
