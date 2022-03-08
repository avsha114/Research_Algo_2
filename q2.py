# We need to save the last input for comparison:
last_input = {}


def lastcall(func: callable):
    def check(*args):
        global last_input
        # Check if the new input equals the last input:
        if args == last_input:
            return f"I already told you that the answer is {func(*args)}"
        else:  # If the input is new - update last input and call func:
            last_input = args
            return func(*args)

    return check


@lastcall
def square(x: int):
    return x ** 2


@lastcall
def case_flip(x: str):
    return x.swapcase()


if __name__ == '__main__':
    # Tests:
    print(square(2))
    print(square(2))
    print(square(3))
    print(square(2))
    print(square(4))
    print(square(4))

    print(case_flip("Hello"))
    print(case_flip("heLlO"))
    print(case_flip("heLlO"))
    print(case_flip("the end"))

    # Expected output:
    # 4
    # I already told you that the answer is 4
    # 9
    # 4
    # 16
    # I already told you that the answer is 16
    # hELLO
    # HElLo
    # I already told you that the answer is HElLo
    # THE END
