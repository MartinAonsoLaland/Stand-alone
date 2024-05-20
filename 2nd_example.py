import numpy as np
def main():

    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    arr1 = np.array([a, b, c])
    arr2 = np.array([2, 5, 7])

    result = arr1 + arr2

    print("Result of addition:", result)

    result = arr1 * arr2

    print("Result of multiplication:", result)


if __name__ == "__main__":
    main()