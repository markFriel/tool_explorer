from utils.decorators import timer


def main():
    y = 2
    second_function(1, 2)
    second_function(1, 2)
    print("Hello from tool-explorer!")


@timer
def second_function(x: int, y: int):
    print("test")
    print("hello world the second")


if __name__ == "__main__":
    y = 1
    main()
