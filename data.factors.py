def find_factors(number):
    factors = []  # Create an empty list to store factors
    for i in range(1, number + 1):  # Loop through numbers starting from 1 to the number itself
        if number % i == 0:  # Check if the number is divisible by i with no remainder
            factors.append(i)  # If it is, add i to the list of factors
    return factors  # Return the list of factors

""" # Example usage:
number = 18
print("The factors of", number, "are:", find_factors(number)) """
