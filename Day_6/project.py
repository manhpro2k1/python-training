## -1
# print out the first 100 items in the sequence, starting from 1
for n in range(1, 101):
    # if n % 15 == 0:
    #     print("Fizz Buzz")
    # elif n % 3 == 0:
    #     print("Fizz")
    # elif n % 5 == 0:
    #     print("Buzz")
    # else:
    #     print(n)

    first = (n % 3 == 0) * "Fizz"
    second = (n % 5 == 0) * "Buzz"
    result = first + second
    print(result or n)
