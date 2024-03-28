class Person:
    def __init__(self, age, weight, height, first_name, last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Weight: {self.weight}, Height: {self.height}"

def get_user_info():
    age = int(input("What's your age: "))
    weight = float(input("What's your weight: "))
    height = float(input("What's your height: "))
    first_name = input("What's your first name: ")
    last_name = input("What's your last name: ")
    return age, weight, height, first_name, last_name

def main():
    age, weight, height, first_name, last_name = get_user_info()
    person = Person(age, weight, height, first_name, last_name)
    if not person.is_adult():
        print("You're not allowed to sign up.")
        return

    state = input("Enter your state (CA/OR/WA): ")
    city = input("Enter your city: ")
    type_of_id = input("What type of ID? (Driver's License / State ID): ")

    if type_of_id.lower() not in ["driver's license", "state id"]:
        print("Pick a valid ID type.")
        return

    print(f"""
Your {type_of_id} will look like this:
{type_of_id.upper()}
{state.upper()}
{city.upper()}

First name, last name:
{first_name.upper()} {last_name.upper()}

Age:
{age}

Height:
{height}

Weight:
{weight}
""")

if __name__ == "__main__":
    main()

