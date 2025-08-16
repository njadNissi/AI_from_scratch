
def show_person(name, age, company):
    print("name = " + name + ", age = " + str(age) + ", comp = " + company)


# show_person("Njad", 10, "Fb")


def show_person(name, age, company="Google"):
    print("name = " + name + ", age = " + str(age) + ", comp = " + company)


# show_person("Njad", 10)


def show_person(name, *, age, company):  # after * param should be specified for each arg
    print("name = " + name + ", age = " + str(age) + ", comp = " + company)


# show_person("Paul", age=10, company="Huawei")


def show_person(name, /, age, company):  # before / param should be specified for each arg
    print("name = " + name + ", age = " + str(age) + ", comp = " + company)


# show_person(name="Njad", 10, "a")


def show_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
    return print(f"Name: {name} Age:{age}")


# show_person("Njad", 150)
