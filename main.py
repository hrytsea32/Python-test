# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    def fun(x):
        print(x)

    lower = 1
    upper = 1000

    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
    fun(5)
