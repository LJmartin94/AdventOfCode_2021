def push_to_z_stack(z, newval):
    z *= 26
    z += newval
    return (z)

def read_from_z_stack(z):
    return (z % 26)


def module_one(w, x, y, z):
    if w != (read_from_z_stack(z) + 11):
        z = push_to_z_stack(z, (w + 6))
    return (w, x, y, z)


def main():
    lines = open("test_input.txt").read().split('\n')
    w = 0  # Input
    x = 0  # Scratch registers
    y = 0  # Scratch registers
    z = 0  # Stack

    tup = module_one(w)
    w = tup[0]
    x = tup[1]
    y = tup[2]
    z = tup[3]


    answer = lines
    print("Answer to 24.0:")
    print(answer)


if __name__ == "__main__":
    main()