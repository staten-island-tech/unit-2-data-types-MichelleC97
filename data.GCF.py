def find_factors(number):
    factors = []
    for i in range(1, number and number_one+ 1):
        if number and number_one % i == 0:
            factors.append(i)
    return factors

number = 18
number_one = 20
print(f"The factors of {number} and {number_one} are: {find_factors(number)}")