'''
_____________LAB5_C____________
1. AI Tool: Gemini (Google)
2. Prompts used:
    "Write a code (Python 3.14) to create a programme to Calculates the dependencies for activities 
    in a process for given data when the dependencies are from the end-to-start 
    (find more information as attached image). 
    Activities are executed in an order or in parallel as paths. 
    Calculates the durations for each path (based on the predecessors and followers). 
    Print the Activities, Paths and Durations. 
'''
from collections import deque, defaultdict


class Activity:
    """Represents a single activity in the project network."""

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.predecessors = []  # List of predecessor names
        self.successors = []   # List of successor objects

        # Time calculation properties (for CPM)
        self.es = 0   # Early Start
        self.ef = 0   # Early Finish
        self.ls = 0   # Late Start
        self.lf = 0   # Late Finish
        self.slack = 0  # Float/slack time

    def __repr__(self):
        return f"Activity({self.name})"


def calculate_cpm(project_activities):
    """Calculates the early and late start/finish times using CPM."""
    # 1. Build the network (graph)
    graph = {name: Activity(name, data['duration'])
             for name, data in project_activities.items()}
    in_degree = defaultdict(int)

    for name, data in project_activities.items():
        if data['predecessors']:
            for pred_name in data['predecessors']:
                if pred_name in graph:
                    graph[pred_name].successors.append(graph[name])
                    graph[name].predecessors.append(pred_name)
                    in_degree[name] += 1
                else:
                    # In a real system, handle the error of a missing predecessor.
                    print(
                        f"Warning: Predecessor '{pred_name}' for activity '{name}' not found.")

    # 2. Forward Pass: Calculate ES and EF
    # Use topological sort for efficient calculation
    queue = deque([act for name, act in graph.items() if in_degree[name] == 0])

    # Starting point(s): ES is 0, EF is duration
    for act in queue:
        act.es = 0
        act.ef = act.duration

    while queue:
        u = queue.popleft()
        for v in u.successors:
            # v.es = max(predecessor_efs)
            v.es = max(v.es, u.ef)
            # v.ef = v.es + v.duration
            v.ef = v.es + v.duration

            # Decrement in-degree and add to queue when it becomes 0
            in_degree[v.name] -= 1
            if in_degree[v.name] == 0:
                queue.append(v)

    # 3. Backward Pass: Calculate LF and LS
    # Find all 'sink' activities (those with no successors)
    max_ef = max(act.ef for act in graph.values())
    sinks = [act for act in graph.values() if not act.successors]

    # Reverse dependency graph for backward traversal
    rev_in_degree = defaultdict(int)
    for act in graph.values():
        rev_in_degree[act.name] = len(act.successors)

    # Starting points for backward pass: sinks
    # LF for sinks = maximum EF found in forward pass
    queue = deque([act for act in sinks if rev_in_degree[act.name] == 0])
    for act in queue:
        act.lf = max_ef
        act.ls = act.lf - act.duration

    while queue:
        v = queue.popleft()  # Current activity
        for pred_name in v.predecessors:
            u = graph[pred_name]  # Predecessor

            # u.lf = min(successor_lss)
            # first successor processed
            if rev_in_degree[u.name] == len(u.successors):
                u.lf = v.ls
            else:
                u.lf = min(u.lf, v.ls)

            u.ls = u.lf - u.duration

            # Decrement rev-in-degree and add to queue when 0
            rev_in_degree[u.name] -= 1
            if rev_in_degree[u.name] == 0:
                queue.append(u)

    # 4. Calculate Slack and mark Critical Activities
    for act in graph.values():
        act.slack = act.lf - act.ef

    return graph


def print_project_summary(graph):
    """Prints a summary table of activities with calculated values."""
    print("---------------------------------------------------------------------------------------")
    print("| Activity | Duration | Early Start | Early Finish | Late Start | Late Finish | Slack |")
    print("---------------------------------------------------------------------------------------")

    # Sort for deterministic output
    sorted_activities = sorted(graph.values(), key=lambda x: x.name)

    for act in sorted_activities:
        print(f"|    {act.name}     |    {act.duration:2}    |    {act.es:2}       |     {act.ef:2}     |     {act.ls:2}     |    {act.lf:2}       |  {act.slack:2}   |")

    print("---------------------------------------------------------------------------------------")
    print(
        f"\nTotal Project Duration: {max(act.ef for act in graph.values())} hours")


# --- Problem Data from Image ---
activity_data = {
    'A': {'duration': 10, 'predecessors': ['C']},
    'B': {'duration': 10, 'predecessors': ['G']},
    'C': {'duration': 5,  'predecessors': []},
    'D': {'duration': 20, 'predecessors': ['A']},
    'E': {'duration': 15, 'predecessors': ['C']},
    'F': {'duration': 10, 'predecessors': ['D', 'H', 'E', 'B']},
    'G': {'duration': 5,  'predecessors': ['C']},
    'H': {'duration': 10, 'predecessors': ['A']}
}

# --- Execute calculations ---
final_graph = calculate_cpm(activity_data)

# --- Output ---
print_project_summary(final_graph)
