def greet():
    """
    simple function that jus prints hello
    :return: None
    """
    print("Hello")

greet()


def greet2(name):
    """
    simple function that greets a persona
    :param name:  the name of a person
    :return: None
    """
    print(f"Hello, {name}")

greet2("Miguel")


def special_op(a=1, b=1):
    """
    speacial op is 10xa+b
    :param a: first number
    :param b: second number
    :return: value, 10a+b
    """
    return 10*a + b

print(special_op(10, 2))
print(special_op(2,10))
result = special_op(8,9)
print(f"The special op for 8 and 9 is: {result}")
print(special_op(b=8,a=9))
print(special_op())
print(special_op(9))

def bond_greet(name):
    print(f"The name is: {name}")

def bondise_name (first_name = "James", last_name = "Bond"):
    return f"{last_name}, {first_name} {last_name}"

print(bondise_name("Miguel", "Tamayo"))
bond_greet(bondise_name("Miguel", "Tamayo"))
bond_greet(bondise_name())