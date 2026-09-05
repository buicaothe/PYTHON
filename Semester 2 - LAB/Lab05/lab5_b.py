# ______________lab5_b___________
def add_card(name, duration, predecessors):
    return {
        'name': name,
        'duration': duration,
        'predecessors': predecessors,
        'followers': []
    }


def build_cards():
    activity_cards = {}
    print("Input the activities (leave empty name to stop):")
    i = 0
    while True:
        name = input(f"Activity name {i}: ").strip()
        if not name:
            break

        # Check Duration (must be an integer)
        while True:
            duration_input = input(f"Duration (hours) for {name}: ").strip()
            if duration_input.isdigit() and int(duration_input) >= 0:
                duration = int(duration_input)
                break
            print("Invalid input! Please enter a non-negative integer for duration.")

        # Input predecessors
        preds_input = input(
            f"Predecessors for {name} (comma separated, leave empty if None): ").strip()
        predecessors = tuple(p.strip()
                             for p in preds_input.split(',')) if preds_input else ()

        activity_cards[i] = add_card(name, duration, predecessors)
        i += 1
    return activity_cards


def show_cards(cards):
    for key, card in cards.items():
        print(f"{key}: {card}")


def calculate_followers(cards):
    start_key = None
    end_keys = []

    for target_key, target_card in cards.items():
        for source_key, source_card in cards.items():
            if target_card['name'] in source_card['predecessors']:
                if source_key not in target_card['followers']:
                    target_card['followers'].append(source_key)

        if not target_card['predecessors']:
            start_key = target_key

    for key, card in cards.items():
        if not card['followers']:
            end_keys.append(key)

    return start_key, end_keys[0] if end_keys else None


def find_all_paths(cards, start_key, end_key):
    all_paths = []

    def dfs(current_key, current_path):
        if current_key == end_key:
            all_paths.append(list(current_path))
            return

        for follower in cards[current_key]['followers']:
            current_path.append(follower)
            dfs(follower, current_path)
            current_path.pop()

    if start_key is not None:
        dfs(start_key, [start_key])
    return all_paths


def build_card_dependencies(cards):
    start_key, end_key = calculate_followers(cards)
    paths_as_keys = find_all_paths(cards, start_key, end_key)

    path_dict = {}
    for i, path in enumerate(paths_as_keys):
        names = [cards[k]['name'] for k in path]
        total_duration = sum(cards[k]['duration'] for k in path)
        path_dict[i] = {
            'keys': path,
            'names': names,
            'tot_duration': total_duration
        }
    return path_dict


def show_paths(path_dict):
    if not path_dict:
        print("No paths found.")
        return

    print("path_dict = {", end="")
    items = list(path_dict.items())
    for i, (key, value) in enumerate(items):
        suffix = "," if i < len(items) - 1 else "}"
        indent = "             " if i > 0 else ""
        print(f"{indent}{key}: {value}{suffix}")
