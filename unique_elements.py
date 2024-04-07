def unique_elements(input_list):
    return list(set(input_list))


def run():
    user_input = input("Enter a list of numbers separated by a space: ")
    numbers = list(map(int, user_input.split()))
    unique_numbers = unique_elements(numbers)
    print("Unique numbers from the entered list: ", unique_numbers)


if __name__ == "__main__":
    run()