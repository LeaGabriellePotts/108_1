def test():
    print("I'm a function")


def say_hello(name):
    print("Hello there" + name)


def sum(num1, num2):
    return num1+num2


result = sum(21, 21)
print("the result of sum(num1, num2) is" + str(result))

# List


def list():
    color = ["red", "green", "blue", "yellow"]
    print(color)

    color.append("white")

    print(len(color))
    color.remove("white")
    print("list")
