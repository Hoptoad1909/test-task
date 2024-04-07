def create_name_age_dict():
    name = input("Enter a name:  ")
    age = int(input("Enter the age:  "))

    name_age_dict = {name: age}
    return name_age_dict


def run():
    name_age_dict = create_name_age_dict()
    print("Dictionary with name and age:", name_age_dict)


if __name__ == "__main__":
    run()
