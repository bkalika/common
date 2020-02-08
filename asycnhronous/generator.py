LIST_OF_NUMBERS = [i for i in range(11)]


def generate_numbers():
    for _ in LIST_OF_NUMBERS:
        yield _


if __name__ == "__main__":
    generator = generate_numbers()
    try:
        while True:
            print(next(generator))
    except StopIteration:
        print("Finish generator's work")
