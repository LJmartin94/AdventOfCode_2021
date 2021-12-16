class Cave:
    def __init__(self, cave_id, cave_size):
        self.cave_id = cave_id
        self.cave_size = cave_size
        self.connected_caves = []


def traverse_caves(cave_str, cave_array, path, all_paths, special_cave):
    cave = go_to_cave(cave_str, cave_array)
    if cave_str == 'end':
        all_paths.append(path)
        return
    for next_cave in cave.connected_caves:
        if next_cave.isupper() or str(path).find(next_cave) == -1:
            p = path.copy()
            p.append(next_cave)
            traverse_caves(next_cave, cave_array, p, all_paths, special_cave)
        elif not special_cave and next_cave != 'start':
            special_cave_copy = next_cave
            p = path.copy()
            p.append(next_cave)
            traverse_caves(next_cave, cave_array, p, all_paths, special_cave_copy)


def go_to_cave(cave_str, cave_array):
    for cave in cave_array:
        if cave.cave_id == cave_str:
            return cave
    return 0


def not_already_included(cave_ids, cave):
    for i in range(len(cave_ids)):
        if cave_ids[i] == cave:
            return 0
    return 1


def main():
    lines = open("input.txt").read().split('\n')
    cave_pairs = []
    for line in lines:
        cave_pairs.append(line.split('-'))
    print(cave_pairs)

    cave_ids = []
    for pair in cave_pairs:
        for cave in pair:
            if not_already_included(cave_ids, cave) == 1:
                cave_ids.append(cave)

    cave_array = []
    for cave in cave_ids:
        size = cave.isupper()
        if size:
            size = "big"
        else:
            size = "small"
        cave_array.append(Cave(cave, size))

    for cave in cave_array:
        for pair in cave_pairs:
            if pair[0] == cave.cave_id:
                cave.connected_caves.append(pair[1])
            if pair[1] == cave.cave_id:
                cave.connected_caves.append(pair[0])

    for cave in cave_array:
        print(cave.cave_id)
        print(cave.cave_size)
        print(cave.connected_caves)
        print()

    path = []
    path.append('start')
    all_paths = []
    special_cave = None
    traverse_caves('start', cave_array, path, all_paths, special_cave)
    i = len(all_paths) - 1
    while i >= 0:
        last_elem = len(all_paths[i]) - 1
        if all_paths[i][last_elem] != 'end':
            all_paths.pop(i)
        i -= 1

    number_of_paths = 0
    for path in all_paths:
        number_of_paths += 1
        print(path)

    answer = number_of_paths
    print("Answer to 12.1:")
    print(answer)


if __name__ == "__main__":
    main()