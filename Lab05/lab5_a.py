import lab5_b as lb


def main():

    # 1. Enter cards:
    activity_cards = lb.build_cards()

    # 2. Printing cards:
    print('\nActivities')
    lb.show_cards(activity_cards)

    # 3. Build dependency paths:
    path_dict = lb.build_card_dependencies(activity_cards)

    # 4. Print the paths:
    print('\nPaths and durations')
    lb.show_paths(path_dict)


if __name__ == "__main__":
    main()
