def filter_numbers_above_13(numbers):
    result = [num for num in numbers if num > 13]
    return result


def run():
    numbers = input("Enter a number list separated by space: ").split()
    numbers = [int(num) for num in numbers]

    filtered_numbers = filter_numbers_above_13(numbers)
    print("Numbers greater than 13:", filtered_numbers)


if __name__ == "__main__":
    run()
