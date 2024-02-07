def divisible_by_5_and_7_generator(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num


def print_divisible_number(n):
    result = list(divisible_by_5_and_7_generator(n))
    print(','.join(map(str, result)))


print_divisible_number(100)

# 2nd Type code #

def divisible_by_5_and_7_generator(n):
    return (num for num in range(0, n+1, 35) if num % 5 == 0 and num % 7 == 0)

def print_divisible_numbers(n):
    result = list(divisible_by_5_and_7_generator(n))
    print(','.join(map(str, result)))


print_divisible_numbers(100)


