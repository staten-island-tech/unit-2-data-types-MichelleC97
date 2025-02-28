def find_factors():
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

number = 1000000
print(f"The factors of{number} are: {find_factors()}")